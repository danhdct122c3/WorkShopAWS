---
title: "Tuần 3: Khởi tạo FastAPI & Cơ sở dữ liệu DynamoDB"
date: 2026-06-22
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---





## 1. Mục tiêu công việc
Khởi tạo FastAPI, cấu trúc thư mục (Router/Service). Áp dụng thiết kế lên Amazon DynamoDB và kết nối thông qua boto3.

## 2. Nhật ký công việc chi tiết

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|---|---|---|---|---|
| 2 | - Khởi tạo FastAPI server theo cấu trúc module hóa (app/modules/).<br>- Thiết lập CORS Middleware và hệ thống Error Handler tập trung. | 06/07/2026 | 06/07/2026 | https://docs.aws.amazon.com/ |
| 3 | - Tích hợp thư viện boto3 để kết nối Backend tới DynamoDB, S3 và Rekognition.<br>- Viết các hàm utilities/helpers phục vụ cho thao tác AWS services. | 07/07/2026 | 07/07/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - Phát triển module `users` và `faces` theo chuẩn Repository – Service – Router.<br>- Viết API phục vụ quản lý thông tin người dùng cơ bản. | 08/07/2026 | 08/07/2026 | https://docs.aws.amazon.com/ |
| 5 | - Phát triển module `attendance` và `notifications`, xử lý nghiệp vụ ghi log điểm danh.<br>- Bổ sung module `reports` và `ai_assistant`, xây dựng mock data để kiểm thử. | 09/07/2026 | 09/07/2026 | https://cloudjourney.awsstudygroup.com/ |
| 6 | - Tổng hợp và cấu hình Swagger UI để tự động sinh tài liệu API (API Docs).<br>- Kiểm thử chéo toàn bộ các endpoint đã phát triển thông qua Swagger UI. | 10/07/2026 | 10/07/2026 | https://docs.aws.amazon.com/ |



## 3. Các kết quả đạt được
- Xây dựng thành công bộ khung FastAPI, hoàn thiện 7 module cốt lõi chuẩn Repository-Pattern và test API qua Swagger.
