---
title: "Member 2 - Backend"
date: 2026-06-22
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

# Work Log: Backend Developer (Member 2)

**Role:** Developing Core APIs using Python/FastAPI, designing Database, and integrating Authentication system.

## Summary of Contributions
Over the course of 8 weeks, I was primarily responsible for building the "brain" of the **Smart Campus** system. Instead of using heavy frameworks (like Spring Boot or Django) running on virtual servers (EC2), I implemented a 100% **Serverless** architecture by packaging **FastAPI** to run directly on **AWS Lambda** via **API Gateway**. This approach allows the project to boot up extremely fast (low Cold start) and costs zero when there is no traffic.

Below is the detailed work log:

## Week 1-2: Database Design & API Initialization
**Tasks:**
- Designed the NoSQL data model on **Amazon DynamoDB**. Analyzed data access patterns to create 5 main tables (`Users`, `Attendance`, `Tasks`, `Leaves`, `Settings`).
- Initialized the Python project using the **FastAPI** framework.
- Configured the `boto3` library to connect the source code with DynamoDB.
- **Challenge:** DynamoDB does not support typical SQL `JOIN` operations, making it difficult to retrieve the Tasks list along with the Employee names (Users).
- **Solution:** Applied Denormalization technique - directly storing `user_name` in the `Tasks` table, and simultaneously configured a **Global Secondary Index (GSI)** for high-speed queries by `assignee_id`.

## Week 3: Building Core APIs (CRUD Modules)
**Tasks:**
- Wrote APIs for the Human Resources Management Module (`POST /users`, `GET /users`, etc.).
- Standardized the source code structure into a 3-tier architecture: `Router` (Receiving requests) -> `Service` (Business logic processing) -> `Repository` (Database interaction).
- **Refactoring:** Converted all data standards from `camelCase` to `snake_case` on the Backend to follow standard Pythonic code (PEP 8). Configured FastAPI to automatically parse responses back to `camelCase` for the Frontend.

## Week 4-5: Complex Business Logic (Rule Engine & Presigned URL)
**Tasks:**
- Built a **Rule Engine** for the Attendance module: Compared employees' check-in time with the standard working hours in the `Settings` table to automatically assign the status `LATE` or `PRESENT`.
- Wrote an API to grant file upload permissions (`/tasks/presigned-url`). This API calls the AWS S3 SDK to generate a temporary link (15 minutes) returned to the Frontend, safely supporting large file uploads (50MB).

## Week 6: Multi-layer Authentication Integration (Amazon Cognito & JWT)
**Tasks:**
- Created an **Amazon Cognito User Pool** on the AWS Console.
- Wrote an API protection layer (`dependencies.py`): Every request sent to the Backend must contain a JWT Token.
- Lambda fetches the Public Key set (JWKS) from Cognito to decrypt and verify the Token's Signature. Only valid tokens are allowed to access the DB.
- Implemented a Role-Based Access Control (RBAC) system: Only `ADMIN` can delete Users, `MANAGER` can approve leave requests, and `STAFF` can only view their own personal information.

## Week 7-8: AWS API Gateway, Logging & CI/CD
**Tasks:**
- Packaged the entire FastAPI code using the `Mangum` library.
- Integrated the Lambda function with **Amazon API Gateway** (Using HTTP API/REST API Proxy Integration).
- Added CORS middleware so the Frontend (running on a different domain) could successfully call the API without being blocked.
- Set up `AWS CodeBuild` to automatically run Unit Tests (`pytest`), package the source code into a `.zip` file, and then automatically update the new version to AWS Lambda (`aws lambda update-function-code`).
