---
title: "Workshop"
date: 2024-01-01
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Triển khai Hệ thống Smart Campus Platform (Serverless) trên AWS

#### Tổng quan

**Smart Campus** là một nền tảng quản lý khuôn viên thông minh 100% Serverless, giải quyết bài toán điểm danh bằng khuôn mặt (AI) và tự động hóa các luồng công việc nhân sự với mức chi phí tối ưu nhất nhờ cơ chế Pay-As-You-Go.

Trong Workshop này, bạn sẽ được hướng dẫn triển khai từ đầu đến cuối (End-to-End) toàn bộ kiến trúc của hệ thống, học cách kết nối và cấu hình bảo mật cho hơn 15 dịch vụ AWS khác nhau, từ Frontend, API, Database, cho đến các luồng Event-Driven và Data Analytics.

Thay vì cấu hình bằng tay (ClickOps), workshop này cũng sẽ hướng dẫn bạn các bước thiết lập chuẩn chỉ, cấu hình các biến môi trường và liên kết các dịch vụ theo đúng nguyên tắc **Đặc quyền tối thiểu (Least Privilege)**.

#### Nội dung Workshop

1. [Giới thiệu tổng quan kiến trúc](5.1-Workshop-overview/)
2. [Chuẩn bị tài nguyên (Prerequisite)](5.2-Prerequiste/)
3. [Phần 1: Cấu hình Xác thực & Bảo mật (Cognito, WAF, IAM)](5.3-Auth-Security/)
4. [Phần 2: Cấu hình Database & Lưu trữ (DynamoDB, S3)](5.4-Database-Storage/)
5. [Phần 3: Cấu hình AI & API (Rekognition, Lambda, API Gateway)](5.5-AI-API/)
6. [Phần 4: Kiến trúc Event-Driven (EventBridge, SQS, SNS/SES)](5.6-Event-Driven/)
7. [Phần 5: Data Pipeline & Analytics (Firehose, Athena)](5.7-Data-Analytics/)
8. [Phần 6: CI/CD Pipeline (CodeBuild, CodePipeline)](5.8-CI-CD-Frontend/)
9. [Phần 7: Giám sát hệ thống (CloudWatch, X-Ray)](5.9-Monitoring-Tracing/)
10. [Phần 8: Kiểm thử & Xác thực (Testing & Validation)](5.10-Testing-Validation/)
11. [Dọn dẹp tài nguyên (Clean-up)](5.11-Cleanup/)
