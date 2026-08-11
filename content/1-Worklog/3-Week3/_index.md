---
title: "Week 3: Initialize FastAPI & DynamoDB Database"
date: 2026-06-22
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---





## 1. Weekly Goals
Initialize FastAPI, define folder structure (Router/Service). Apply the database design to Amazon DynamoDB and connect via boto3.

## 2. Detailed Work Log

| Day | Task Description | Start Date | End Date | References |
|---|---|---|---|---|
| Mon | - Initialize Virtual Environment. Install required libraries: FastAPI, Boto3. Set up module structure. | 06/07/2026 | 06/07/2026 | AWS Docs / Github |
| Tue | - Deploy the data model to Amazon DynamoDB with 5 main tables: Users, Tasks, Leaves, Attendance, Settings. | 07/07/2026 | 07/07/2026 | StackOverflow |
| Wed | - Write Repository classes configuring Boto3 Resource. Handle data conversion from Python to DynamoDB. | 08/07/2026 | 08/07/2026 | API Docs |
| Thu | - Define Pydantic Schemas to validate input data (Data Validation). | 09/07/2026 | 09/07/2026 | AWS Blogs |
| Fri | - Write the API flow to register and retrieve HR information (CRUD Users) following the Controller - Service model. | 10/07/2026 | 10/07/2026 | Weekly Report |


## 3. Achievements
- Successfully built FastAPI framework, completed 7 core modules with Repository-Pattern and tested APIs via Swagger.
