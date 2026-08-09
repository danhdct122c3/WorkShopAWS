---
title : "Prerequisites"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

To begin deploying the **Smart Campus Platform**, you need to prepare some basic tools and resources on the AWS environment.

### 1. AWS Account
- You need an AWS account with administrator privileges (`AdministratorAccess`).
- If you are using a newly created account (Free Tier), this Serverless system is designed to fall entirely within the AWS free tier limits, ensuring you incur no costs during practice.
- **Recommended Region:** Select the `ap-southeast-1` (Singapore) region for the lowest latency to Vietnam.

### 2. Prepare Basic IAM Roles
In this system, AWS services need to communicate with each other (e.g., Lambda calls Rekognition, API Gateway calls Lambda). To ensure the **Least Privilege** principle, we will create specific IAM Roles at each practical step. However, for now, you need to understand the principle:
- Do not use hard-coded Access Keys / Secret Keys in your code.
- All communication permissions are granted via **IAM Roles**.

### 3. Install Local Tools
Although you can configure the entire system using the UI (AWS Console), installing the tools below will help you test APIs and manage source code more easily:
- **Visual Studio Code (VSCode):** To read and edit Frontend (React) and Backend (Python/FastAPI) source code.
- **Postman** or **Thunder Client**: Used to test the API Endpoints we are about to create on Amazon API Gateway.
- **Git:** Necessary to push source code to the repository and integrate with AWS CodePipeline later.

### 4. Project Source Code
Please clone (download) the standard source code of the Smart Campus project to your personal computer to use for the next steps:

```bash
git clone https://github.com/your-username/smart-campus-serverless.git
cd smart-campus-serverless
```
*(The source code directory structure will consist of 2 main parts: `/frontend` containing ReactJS code and `/backend` containing Python code for Lambda).*

---
Once prepared, move on to the next lesson to start **Part 1: Multi-layer Security & Authentication Setup**.