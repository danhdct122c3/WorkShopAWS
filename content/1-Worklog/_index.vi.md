---
title: "Nhật ký công việc"
date: 2026-06-22
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

# Nhật Ký Công Việc (Worklog)

## Tổng Quan Chương Trình Thực Tập

Chương trình thực tập tại **FCAJ (First Cloud AI Journey)** kéo dài **8 tuần**, từ ngày **22/06/2026** đến **15/08/2026**. Trong suốt thời gian này, nhóm chúng em (gồm 4 thành viên) đã phối hợp xây dựng hoàn chỉnh dự án **Smart Campus Platform** — một hệ thống **quản lý công việc và điểm danh** cho doanh nghiệp theo kiến trúc **Serverless & Event-Driven** trên nền tảng AWS.

## Kiến trúc Dự án & Phân công Công việc

Dự án sử dụng hơn **10 dịch vụ AWS** tích hợp chặt chẽ với nhau. Để tối ưu hóa quá trình phát triển, nhóm đã chia khối lượng công việc thành 4 mảng chính tương ứng với 4 thành viên:

| Vai trò | Trách nhiệm chính | Dịch vụ AWS sử dụng |
|---------|-------------------|---------------------|
| **Member 1 (Frontend)** | Giao diện ReactJS, Tích hợp API, Trải nghiệm người dùng | S3 (Static Web), CloudFront |
| **Member 2 (Backend)** | Core API (FastAPI), Database, Xác thực người dùng | API Gateway, Lambda, DynamoDB, Cognito |
| **Member 3 (AI & Analytics)** | Nhận diện khuôn mặt, Phân tích dữ liệu lớn | Rekognition, S3 Data Lake, Glue, Athena |
| **Member 4 (Cloud & DevOps)** | Event-Driven, Thông báo, CI/CD, Giám sát hệ thống | EventBridge, SQS, SNS/SES, CodePipeline, CloudWatch |

## Nhật ký Công việc Chi tiết (Theo Thành viên)

Dưới đây là nhật ký công việc chi tiết của từng thành viên trong suốt 8 tuần thực tập. Mỗi báo cáo ghi rõ tiến độ, khó khăn gặp phải và giải pháp xử lý theo từng tuần:

**Vai trò 1:** [Member 1 - Frontend Developer](1.1-member-1-frontend/)

**Vai trò 2:** [Member 2 - Backend Developer](1.2-member-2-backend/)

**Vai trò 3:** [Member 3 - AI & Data Analytics Engineer](1.3-member-3-ai-analytics/)

**Vai trò 4:** [Member 4 - Cloud & DevOps Engineer](1.4-member-4-cloud-devops/)