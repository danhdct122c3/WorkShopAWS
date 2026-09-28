---
title: "Tuần 8: Tổng kết dự án & Viết Báo Cáo"
date: 2026-06-22
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---





## 1. Mục tiêu công việc
Hoàn thiện tài liệu báo cáo thực tập, quay video demo, thiết kế slide thuyết trình và chuẩn bị cho buổi bảo vệ đồ án cuối khóa.

## 2. Nhật ký công việc chi tiết

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|---|---|---|---|---|
| 2 | - Tích hợp AWS X-Ray SDK (Distributed Tracing) bằng hàm `patch_all()` trong FastAPI.<br>- Theo dõi toàn bộ lời gọi boto3 tới DynamoDB, Rekognition, S3 trên X-Ray Console. | 10/08/2026 | 10/08/2026 | https://docs.aws.amazon.com/ |
| 3 | - Xử lý sự cố xung đột Segment X-Ray trên môi trường AWS Lambda bằng middleware.<br>- Thiết lập CloudWatch Alarm theo dõi metric Errors (5xx) của Lambda backend. | 11/08/2026 | 11/08/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - Cấu hình kết nối CloudWatch Alarm với SNS Topic để gửi email cảnh báo khi crash.<br>- Phân tách logic bắt lỗi 4xx khỏi 5xx để tránh False Alarm. | 12/08/2026 | 12/08/2026 | https://docs.aws.amazon.com/ |
| 5 | - Triển khai kiến trúc Amazon SQS: Chèn SQS làm Buffer giữa EventBridge và Lambda.<br>- Tạo queue xử lý Analytics, Notification và cấu hình Partial Batch Response. | 13/08/2026 | 13/08/2026 | https://cloudjourney.awsstudygroup.com/ |
| 6 | - Thiết lập Dead Letter Queue (DLQ) hứng message lỗi để retry tự động.<br>- Rà soát source code Backend, đóng gói artifacts và hoàn tất báo cáo kỹ thuật. | 14/08/2026 | 14/08/2026 | https://docs.aws.amazon.com/ |



## 3. Các kết quả đạt được
- Hệ thống Backend đạt tiêu chuẩn production với X-Ray Tracing, CloudWatch Alarms và kiến trúc SQS Buffer mạnh mẽ.
