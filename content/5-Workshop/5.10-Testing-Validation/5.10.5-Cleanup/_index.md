---
title : "Resource Cleanup"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 5.10.5. </b> "
---

#### Resource Cleanup (Clean-up)

> [!CAUTION]
> After completing the Workshop, please delete all created resources to **avoid incurring unwanted costs** on your AWS account.

Below is the list of resources to delete in a safe order (delete dependent resources first):

---

**Step 1: Delete CloudFront Distributions**

1. Go to **CloudFront** > **Distributions**.
2. Select the `smart-campus-frontend` distribution (from lesson 5.8.3):
   - Click **Disable** and wait for the status to change to `Disabled`.
> ![Disable CloudFront](/aws-image/setupCleanup/cleanupcloudfront1.png)
   - Then click **Delete**.
> ![Delete CloudFront](/aws-image/setupCleanup/cleanupcloudfront2.png)
3. Do the same with the `smart-campus-api-cf` distribution (from lesson 5.5.4).

---

**Step 2: Delete CodePipeline and CodeBuild**

1. Go to **CodePipeline** > Select `smart-campus-backend-pipeline` > Click **Delete pipeline**.
> ![Delete Pipeline](/aws-image/setupCleanup/cleanupipeline1.png)
2. Next, delete `smart-campus-frontend-pipeline`.
3. Go to **CodeBuild** > Delete the projects `smart-campus-backend-build` and `smart-campus-frontend-build`.
> ![Delete CodeBuild](/aws-image/setupCleanup/cleanupcodebuild1.png)

---

**Step 3: Delete API Gateway**

1. Go to **API Gateway** > Select the `SmartCampusHTTPApi` API > Click **Delete**.
> ![Delete API 1](/aws-image/setupCleanup/cleanupapi1.png)
> ![Delete API 2](/aws-image/setupCleanup/cleanupapi2.png)

---

**Step 4: Delete Lambda Functions**

1. Go to **Lambda** > **Functions**.
2. Delete one by one:
   - `smart-campus-api`
   - `smart-campus-analytics-worker`
> ![Delete Lambda 1](/aws-image/setupCleanup/cleanuplambda1.png)
> ![Delete Lambda 2](/aws-image/setupCleanup/cleanuplambda2.png)

---

**Step 5: Delete EventBridge Rules**

1. Go to **Amazon EventBridge** > **Rules**.
2. Delete `attendance-recorded-to-sns` and `attendance-to-sqs`.
> ![Delete EventBridge](/aws-image/setupCleanup/cleanupevenbridge1.png)

---

**Step 6: Delete SQS Queues**

1. Go to **SQS** > Delete `smart-campus-analytics-queue`.
2. Next, delete `smart-campus-dlq`.
> ![Delete SQS](/aws-image/setupCleanup/cleanupsqs1.png)

---

**Step 7: Delete SNS Topics**

1. Go to **SNS** > **Topics** > Delete `smart-campus-notifications`.
> ![Delete SNS 1](/aws-image/setupCleanup/cleanupsns1.png)
2. Go to **Subscriptions** > Delete related Subscriptions.
> ![Delete SNS 2](/aws-image/setupCleanup/cleanupsns2.png)

---

**Step 8: Delete CloudWatch Alarms and Log Groups**

1. Go to **CloudWatch** > **Alarms** > Delete the alarm `Lambda-Error-Alert`.
> ![Delete Alarms 1](/aws-image/setupCleanup/cleanupcloudwatch1.png)
> ![Delete Alarms 2](/aws-image/setupCleanup/cleanupcloudwatch5.png)
2. Go to **Log groups** > Delete `/aws/lambda/smart-campus-api` and `/aws/lambda/smart-campus-analytics-worker`.
> ![Delete Log Groups 1](/aws-image/setupCleanup/cleanupcloudwatch2.png)
> ![Delete Log Groups 2](/aws-image/setupCleanup/cleanupcloudwatch3.png)
> ![Delete Log Groups 3](/aws-image/setupCleanup/cleanupcloudwatch4.png)
3. Go to **WAF Logs** > Delete log group `aws-waf-logs-smartcampus`.

---

**Step 9: Delete WAF Web ACL**

1. Go to **WAF & Shield** > **Web ACLs** (select Global/CloudFront scope).
2. Delete `SmartCampusAPIWebACL`.
> ![Delete WAF 1](/aws-image/setupCleanup/cleanupwaf1.png)
3. Go to **IP sets** > Delete `SmartCampusIPSet`.
> ![Delete WAF 2](/aws-image/setupCleanup/cleanupwaf2.png)

---

**Step 10: Delete DynamoDB Tables**

1. Go to **DynamoDB** > **Tables**.
2. Delete all tables one by one: `smart-campus-attendance`, `smart-campus-faces`, `smart-campus-users`, `smart-campus-security`, `smart-campus-notifications`, `smart-campus-settings`, `smart-campus-tasks`, `smart-campus-leaves`, `smart-campus-holidays`.
> ![Delete DynamoDB](/aws-image/setupCleanup/cleanupdynamodb1.png)

---

**Step 11: Delete S3 Buckets**

> [!WARNING]
> You must **delete all objects inside** before you can delete a bucket.

1. Go to **S3**, for each following bucket:
   - `smart-campus-images-{id}`
   - `smart-campus-frontend-2026`
   - `smart-campus-datalake-{id}`
   - Bucket saving Athena results
2. Go inside the bucket > Select all objects > **Delete**.
> ![Empty S3 1](/aws-image/setupCleanup/cleanups31.png)
> ![Empty S3 2](/aws-image/setupCleanup/cleanups32.png)
3. Then exit and delete the bucket.
> ![Delete S3 3](/aws-image/setupCleanup/cleanups33.png)

---

**Step 12: Delete Rekognition Collection**

Open **AWS CloudShell** and run the command:
```bash
aws rekognition delete-collection --collection-id smart-campus-faces --region ap-southeast-1
```

---

**Step 13: Delete Cognito User Pool**

1. Go to **Amazon Cognito** > **User Pools**.
2. Select the User Pool you created > Click **Delete**.
> ![Delete Cognito](/aws-image/setupCleanup/cleanupcognito1.png)

---

**Step 14: Delete IAM Roles**

1. Go to **IAM** > **Roles**.
2. Delete the roles: `smart-campus-api-role-...`, `smart-campus-analytics-worker-role-...`, `AWSGlueServiceRole-SmartCampus`, and roles automatically created by CodeBuild/CodePipeline.
> ![Delete IAM](/aws-image/setupCleanup/cleanupiam1.png)

---

**Step 15: Delete Glue Crawler and Database**

1. Go to **AWS Glue** > **Crawlers** > Delete `smart-campus-attendance-crawler`.
> ![Delete Glue Crawler](/aws-image/setupCleanup/cleanupglue1.png)
2. Go to **Databases** > Delete `smart_campus_db`.
> ![Delete Glue Database](/aws-image/setupCleanup/cleanupglue2.png)

---

### ✅ Check Completion

After finishing deletion, go to **AWS Cost Explorer** or **Billing Dashboard** to confirm that no resources are running and incurring costs. Congratulations on completing the entire **Smart Campus Platform on AWS** Workshop! 🎉
