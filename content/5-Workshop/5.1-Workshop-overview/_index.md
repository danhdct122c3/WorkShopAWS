---
title : "Overview"
date : 2024-01-01 
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

### 1. Solution Overview (Use case)
In the context of digital transformation in education and enterprises, manual attendance tracking (magnetic cards, fingerprints) still has major limitations (pain points): congestion during peak hours, forgotten cards, or proxy check-ins. Internal physical server systems often waste resources when not in use at night, but become overloaded at 8:00 AM.

**Smart Campus Platform** was created to completely solve this problem by combining facial recognition AI (**Amazon Rekognition**) and a **100% AWS Serverless** architecture. The system not only processes attendance at high speed but also ensures absolute security, automates notification workflows, and provides Big Data analytics solutions with optimized costs (Pay-as-you-go).

### 2. Architecture Diagram
The architecture of the Smart Campus system includes the following blocks: Frontend & Edge, Authentication, Core API & AI, Asynchronous Event-Driven, Data Analytics, CI/CD Pipeline, and Observability.

> **Figure 1 - Architecture Diagram and Smart Campus Workflow**
> ![Architecture Overview](/aws-image/Architechture.png)

**Overall system processing flow:**
`Frontend -> CloudFront -> API Gateway -> Lambda -> Rekognition -> DynamoDB -> EventBridge -> SQS -> Lambda Worker -> SNS/SES`
Simultaneously: `EventBridge -> Kinesis Firehose -> S3 Data Lake -> Athena`

### 3. Main Flow and Asynchronous Architecture
One of the key and most important points of this architecture is **the application of Asynchronous processing for tasks that do not require immediate responses**.

**Why choose asynchronous processing?**
Attendance tracking at the beginning of the day or at the end of shifts creates a massive amount of traffic at the same time (Spike Traffic). If everything is processed synchronously (saving to DB, compressing logs, sending late warning emails...), the system will respond very slowly or create bottlenecks. Separating the reporting and notification workflows from the main attendance flow (via EventBridge and SQS) allows the API to respond to users within milliseconds, while heavy tasks are pushed into a buffer queue to be processed reliably over time.

**The End-to-End Main Flow occurs in detail through 16 steps (as numbered in the diagram):**

*   **(1) User access via WAF:** The user opens the frontend web application. Requests pass through the AWS WAF firewall (blocking malicious IPs, DDoS) and CloudFront CDN to load static content from S3.
*   **(2) Login / Cognito:** The user logs into the system and receives a JWT authentication token from Amazon Cognito.
*   **(3) API Gateway receives the request:** The interface calls the attendance API, sending the JWT Token. API Gateway will automatically validate this token.
*   **(4) Call Lambda Core:** After successful authentication, the request is proxied to AWS Lambda (Core Logic) to begin business processing.
*   **(5) Face Matching:** Lambda calls the Amazon Rekognition API to match the submitted facial image with the original facial database.
*   **(6) Save original image:** For auditing and verification purposes, the photo taken during attendance is saved by Lambda to the Raw Images S3 bucket.
*   **(7) Save attendance status:** If the faces match, Lambda saves the attendance record (Check-in/out) to Amazon DynamoDB.
*   **(8) Emit Event (Attendance Event):** Immediately after saving to the DB, Lambda emits a successful/failed attendance event to the Amazon EventBridge Event Bus. The API returns the result to the Frontend instantly.
*   **(9) Queueing:** EventBridge routes the event into an Amazon SQS queue serving as a buffer to prevent bottlenecks.
*   **(10) Lambda Worker processing:** A background Lambda function retrieves events from the SQS Queue to process time-consuming tasks.
*   **(11) Send alerts:** Lambda Worker calls Amazon SNS and Amazon SES to send messages/emails (e.g., late staff notifications or spoofing alerts).
*   **(12) Push logs (Streaming):** Simultaneously at step 8, EventBridge also routes this log event to Amazon Kinesis Data Firehose for analysis purposes.
*   **(13) Batching & Writing Data:** Firehose automatically batches and compresses the log data, writing it as files into the S3 Data Lake Bucket.
*   **(14) Query & Reporting:** The HR Director uses Amazon Athena (via SQL commands) or BI Tools to generate statistical reports directly from the Data Lake without touching DynamoDB.
*   **(15) Monitoring & Alarm:** The entire operational process (Logs & Metrics) is recorded in Amazon CloudWatch. If an error is detected (e.g., Lambda crash), CloudWatch Alarms will immediately alert the Ops Team via Email/Chat.
*   **(16) Automated CI/CD Deploy:** Developers' code changes will go through AWS CodePipeline and AWS CodeBuild to automatically build and deploy (Serverless Deploy) to the AWS infrastructure without manual intervention.

### 4. In-Scope Services (MVP Scope)
To complete this lab, the primary AWS services used include:
- **Edge & Frontend:** Amazon S3 (Static Website), Amazon CloudFront, AWS WAF.
- **Authentication & API:** Amazon Cognito, Amazon API Gateway.
- **Core Compute & AI:** AWS Lambda, Amazon Rekognition.
- **Database & Storage:** Amazon DynamoDB, Amazon S3.
- **Event & Queue:** Amazon EventBridge, Amazon SQS, Amazon SNS/SES.
- **Data Analytics:** Amazon Kinesis Data Firehose, Amazon Athena, AWS Glue.
- **CI/CD & Observability:** AWS CodeBuild, AWS CodePipeline, Amazon CloudWatch.
- **Security:** AWS IAM.

### 5. Expected Outcomes upon Workshop Completion
At the end of this practical series, you will have built a complete enterprise platform:
- **Fully functional Frontend:** Features an attendance interface and a management dashboard.
- **Multi-layer security authentication:** Prevents spoofing using IAM Least Privilege, WAF, and Cognito JWT.
- **High-load resilient architecture:** Proficiently applies Event-Driven design (EventBridge + SQS) to eliminate peak hour bottlenecks.
- **Automated Data Pipeline:** Owns a Data Lake system (Firehose + Athena) that completely separates OLTP and OLAP.
- **DevOps CI/CD:** A CodePipeline system that automatically builds and deploys code without manual intervention.
- **Cleanup:** Capable of quickly cleaning up resources to fully control AWS costs.