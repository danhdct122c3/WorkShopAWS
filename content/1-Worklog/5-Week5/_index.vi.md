---
title: "Tuần 5: Xử lý Upload file (Presigned URL)"
date: 2026-06-22
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---





## 1. Mục tiêu công việc
Xử lý bài toán upload bằng cách cấp phát Presigned URL (AWS S3) thay vì tải qua API Gateway để tránh timeout và limit dung lượng.

## 2. Nhật ký công việc chi tiết

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|---|---|---|---|---|
| 2 | - Hoàn thiện module Notifications với 5 Message Template (Attendance, Security, v.v.).<br>- Tích hợp Amazon SNS ARN để đẩy thông báo đa kênh, ghi Audit Trail vào DynamoDB. | 20/07/2026 | 20/07/2026 | https://docs.aws.amazon.com/ |
| 3 | - Xây dựng luồng xử lý sự kiện: Lambda Worker lắng nghe EventBridge và gọi SNS.<br>- Triển khai Analytics Pipeline (Phase 1): Viết API truy vấn trực tiếp từ DynamoDB. | 21/07/2026 | 21/07/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - Triển khai Analytics (Phase 2): Dựng Data Lake bằng Lambda stream tới Kinesis Firehose.<br>- Đẩy dữ liệu xuống S3 phân vùng động (year/month) và chạy AWS Glue Crawler. | 22/07/2026 | 22/07/2026 | https://docs.aws.amazon.com/ |
| 5 | - Viết câu truy vấn SQL chuẩn qua Amazon Athena để lấy dữ liệu thống kê từ S3.<br>- Xây dựng 4 REST endpoint cho Analytics (summary, daily, trend) với fallback. | 23/07/2026 | 23/07/2026 | https://cloudjourney.awsstudygroup.com/ |
| 6 | - Phát triển module Quản lý công việc (Tasks) với cấu trúc 13 attributes và 3 GSI.<br>- Vá bug schema Notification dùng camelCase bị DynamoDB từ chối ghi ngầm. | 24/07/2026 | 24/07/2026 | https://docs.aws.amazon.com/ |



## 3. Các kết quả đạt được
- Triển khai thành công Data Lake (Firehose, Glue, Athena) và hệ thống thông báo sự kiện qua SNS.
