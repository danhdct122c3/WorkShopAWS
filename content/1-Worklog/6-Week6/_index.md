---
title: "Week 6: Integrate Multi-factor Authentication (Cognito)"
date: 2026-06-22
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

# Week 6: Integrate Multi-factor Authentication (Cognito)

**Team Member:** Backend Developer

## 1. Weekly Goals
Create an Amazon Cognito User Pool. Write middleware to block APIs, only allowing requests with valid JWT Tokens to pass.

## 2. Detailed Work Log

| Day | Task Description | Start Date | End Date | References |
|---|---|---|---|---|
| Mon | - Set up Amazon Cognito User Pool. Configure security policies (Password policy). | 27/07/2026 | 27/07/2026 | AWS Docs / Github |
| Tue | - Write an automated sync script: Adding a new User to DynamoDB will auto-create an account in Cognito. | 28/07/2026 | 28/07/2026 | StackOverflow |
| Wed | - Build the API protection layer (Dependency Auth). Fetch Public Keys (JWKS) from Cognito to cache locally. | 29/07/2026 | 29/07/2026 | API Docs |
| Thu | - Use the python-jose library to decode and verify the JWT Access Token Signature. | 30/07/2026 | 30/07/2026 | AWS Blogs |
| Fri | - Attach Dependency Auth to Endpoints. Declare Security Schema to test directly on Swagger UI. | 31/07/2026 | 31/07/2026 | Weekly Report |


## 3. Achievements
- Completed features and objectives set for the week.
- Successfully integrated with related AWS services (if any).
- Ensured work quality meets project requirements.

## 4. Challenges & Solutions
- **Challenges:** The research and integration process occasionally encountered unexpected errors. Required significant time reading logs and AWS technical documentation.
- **Solutions:** Coordinated with other team members for discussions, thoroughly read the guidelines, and sought additional advice from Mentors.

## 5. Plan for Next Week
- Review this week's completed work.
- Begin research and implementation of tasks for Week 7.
