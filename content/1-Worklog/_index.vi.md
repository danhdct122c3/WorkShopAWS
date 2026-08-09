---
title: "Nhật ký công việc"
date: 2026-06-22
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

# Nhật Ký Công Việc (Worklog)

## Tổng Quan Chương Trình Thực Tập

Chương trình thực tập tại **FCAJ (First Cloud AI Journey)** kéo dài **8 tuần**, từ ngày **22/06/2026** đến **15/08/2026**. Trong suốt thời gian này, em đã xây dựng hoàn chỉnh dự án **Smart Campus Platform** — một hệ thống **quản lý công việc và điểm danh** cho doanh nghiệp theo kiến trúc **Serverless & Event-Driven** trên nền tảng AWS.

## Kiến trúc Dự án

Dự án sử dụng hơn **10 dịch vụ AWS** tích hợp chặt chẽ với nhau:

| Nhóm | Dịch vụ AWS | Vai trò |
|------|-------------|---------|
| **Compute** | Lambda, API Gateway | Backend Serverless |
| **Database** | DynamoDB, Athena | Lưu trữ & Phân tích dữ liệu |
| **Storage** | S3 | Lưu ảnh khuôn mặt, Data Lake |
| **AI/ML** | Rekognition, Bedrock | Nhận diện khuôn mặt, AI Chat |
| **Messaging** | EventBridge, SNS, SQS | Event-Driven, Thông báo, Message Queue |
| **Security** | Cognito, IAM, WAF | Xác thực, Phân quyền, Bảo mật |
| **Monitoring** | CloudWatch, X-Ray | Giám sát, Truy vết |
| **Analytics** | Glue, Athena | Data Pipeline, Báo cáo |

## Tóm tắt 8 Tuần Thực Tập

| Tuần | Thời gian | Nội dung chính | Kết quả |
|------|-----------|----------------|---------|
| **1** | 22/06 – 27/06 | Lý thuyết Cloud, IAM, Serverless, EventBridge | Thiết lập môi trường AWS, chạy Lambda đầu tiên |
| **2** | 30/06 – 04/07 | Phân tích nghiệp vụ, thiết kế kiến trúc 8 WF | Hoàn tất tài liệu kiến trúc, khởi tạo DynamoDB |
| **3** | 07/07 – 11/07 | Backend FastAPI 7 modules + Frontend Glassmorphism | CRUD Users end-to-end hoàn chỉnh |
| **4** | 14/07 – 18/07 | Rekognition (WF2) + Rule Engine Điểm danh (WF3) | Face Registration & Attendance hoàn chỉnh |
| **5** | 21/07 – 25/07 | SNS Notifications (WF4) + Athena Analytics (WF5) + Tasks (WF8) | 3 Workflows + Dashboard hoàn chỉnh |
| **6** | 28/07 – 01/08 | Cognito Auth + Đăng nhập khuôn mặt + Analytics RBAC | Bảo mật 2 lớp + SVG Donut Chart |
| **7** | 04/08 – 08/08 | Leave Management + Toast UI + Chuẩn hóa RBAC | Nghỉ phép + Interactive Calendar |
| **8** | 11/08 – 15/08 | X-Ray + CloudWatch + SQS + Workshop Docs | Giám sát hoàn chỉnh + Đồ án tổng kết |

## Các Tuần Chi Tiết

**Tuần 1:** [Lý thuyết & Khái niệm nền tảng AWS](1.1-Week1/)

**Tuần 2:** [Phân tích nghiệp vụ & Thiết kế kiến trúc dự án](1.2-Week2/)

**Tuần 3:** [Xây dựng Backend Core & Frontend Khung](1.3-Week3/)

**Tuần 4:** [Nhận diện Khuôn mặt & Hệ thống Điểm danh](1.4-Week4/)

**Tuần 5:** [Thông báo, Analytics Pipeline & Quản lý Công việc](1.5-Week5/)

**Tuần 6:** [Xác thực, Bảo mật & Giao diện Nâng cao](1.6-Week6/)

**Tuần 7:** [Quản lý Nghỉ phép & Hoàn thiện Hệ thống](1.7-Week7/)

**Tuần 8:** [Giám sát, Độ tin cậy & Workshop Documentation](1.8-Week8/)