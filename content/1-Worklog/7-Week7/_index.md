---
title: "Week 7: Role-Based Access Control (RBAC) & API Gateway"
date: 2026-06-22
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---





## 1. Weekly Goals
Implement Admin, Manager, Staff authorization. Package source code (Mangum) and integrate with Amazon API Gateway.

## 2. Detailed Work Log

| Day | Task Description | Start Date | End Date | References |
|---|---|---|---|---|
| Mon | - Design Role-Based Access Control (RBAC). Write advanced authorization functions (Authorization Decorator). | 03/08/2026 | 03/08/2026 | AWS Docs / Github |
| Tue | - Develop business authorization logic: Approve department leave requests, secure personal information. | 04/08/2026 | 04/08/2026 | StackOverflow |
| Wed | - Install the Mangum library. Wrap the FastAPI app with Mangum to run on Serverless environments. | 05/08/2026 | 05/08/2026 | API Docs |
| Thu | - Set up Lambda Function (Memory, Timeout) and configure Amazon API Gateway (HTTP API). | 06/08/2026 | 06/08/2026 | AWS Blogs |
| Fri | - Clean up dead code, update `requirements.txt`. Assist DevOps in writing pytest for CI/CD pipeline. | 07/08/2026 | 07/08/2026 | Weekly Report |


## 3. Achievements
- Completed Leave Management module with complex anti-overlap checking logic and attendance event synchronization.
