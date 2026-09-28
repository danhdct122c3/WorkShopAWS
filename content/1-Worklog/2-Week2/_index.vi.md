---
title: "Tuần 2: Phân tích Nghiệp vụ & Sơ đồ ERD"
date: 2026-06-22
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---





## 1. Mục tiêu công việc
Phân tích yêu cầu bài toán. Thiết kế mô hình dữ liệu (ERD) NoSQL trên giấy, xác định các PK và GSI.

## 2. Nhật ký công việc chi tiết

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|---|---|---|---|---|
| 2 | - Cập nhật yêu cầu đồ án Smart Campus, xác định các nhóm user và use-case.<br>- Bắt đầu phân tích bài toán Backend và định hình các dịch vụ AWS cần thiết. | 29/06/2026 | 29/06/2026 | https://docs.aws.amazon.com/ |
| 3 | - Thiết kế kiến trúc tổng thể hệ thống theo hướng Event-Driven Serverless.<br>- Định nghĩa 8 luồng nghiệp vụ cốt lõi (Auth, Face, Attendance, Notification, v.v.). | 30/06/2026 | 30/06/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - Khởi tạo dự án theo cấu trúc Monorepo, cài đặt môi trường Python 3.11+.<br>- Xây dựng tài liệu kiến trúc Backend chi tiết và thống nhất stack công nghệ. | 01/07/2026 | 01/07/2026 | https://docs.aws.amazon.com/ |
| 5 | - Khởi tạo thủ công 5 bảng cơ sở dữ liệu trên DynamoDB qua AWS Console.<br>- Thiết lập S3 Bucket và Amazon Rekognition Collection cho xử lý hình ảnh. | 02/07/2026 | 02/07/2026 | https://cloudjourney.awsstudygroup.com/ |
| 6 | - Hoàn thiện tài liệu thiết kế database (ERD) và các kịch bản API Backend.<br>- Rà soát, chuẩn bị các library cần thiết (boto3, FastAPI) cho tuần tiếp theo. | 03/07/2026 | 03/07/2026 | https://docs.aws.amazon.com/ |



## 3. Các kết quả đạt được
- Khởi tạo xong Monorepo Python, cấu hình xong hạ tầng AWS cơ bản (DynamoDB, S3, Rekognition) và chốt kiến trúc.
