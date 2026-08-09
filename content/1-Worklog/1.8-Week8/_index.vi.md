---
title: "Worklog Tuần 8"
date: 2026-08-09
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Mục tiêu tuần 8:

* Triển khai hệ thống Giám sát & Quan sát toàn diện (AWS X-Ray, CloudWatch, SNS Alerting).
* Nâng cấp độ tin cậy hệ thống với Amazon SQS làm Buffer ngăn mất dữ liệu khi Spike Traffic.
* Nghiên cứu và thiết kế tính năng chống gian lận điểm danh (Face Liveness Detection).
* Hoàn tất viết tài liệu Workshop và chuẩn bị báo cáo thu hoạch tổng kết Đồ án.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|-----|-----------|--------------|-----------------|----------------|
| 2 | - Tích hợp **AWS X-Ray** (Distributed Tracing): <br>&emsp; + Thêm `aws-xray-sdk` vào `requirements.txt`. <br>&emsp; + Gọi `patch_all()` trong `main.py` để X-Ray tự động theo dõi mọi lần gọi boto3 (DynamoDB, Rekognition, S3). <br>&emsp; + Fix bug Segment xung đột trên Lambda: Gỡ bỏ `XRayMiddleware` vì Lambda đã tự tạo root Segment. <br>&emsp; + Kiểm tra Service Map và Trace Timeline trên AWS X-Ray Console. | 11/08/2026 | 11/08/2026 | https://docs.aws.amazon.com/xray/ |
| 3 | - Thiết lập **CloudWatch Alarm + SNS Alerting**: <br>&emsp; + Cấu hình CloudWatch Alarm theo dõi metric `Errors` của Lambda `smart-campus-api`. <br>&emsp; + Liên kết Alarm với SNS Topic → Gửi Email cảnh báo về hòm thư Admin trong vòng 5 phút khi Lambda crash. <br>&emsp; + Phân biệt: Lỗi hệ thống (5xx) kích hoạt Alarm; Lỗi người dùng (4xx) được bắt và loại bỏ (không gây False Alarm). <br> - Kiểm tra bằng cách cố tình gây lỗi Lambda và xác nhận email cảnh báo đến đúng hộp thư. | 12/08/2026 | 12/08/2026 | https://docs.aws.amazon.com/cloudwatch/ |
| 4 | - Triển khai **Amazon SQS** (Message Queue Architecture): <br>&emsp; + Vấn đề: EventBridge đẩy thẳng vào Lambda → Nguy cơ mất dữ liệu khi Spike Traffic. <br>&emsp; + Giải pháp: Chèn SQS vào giữa EventBridge và Lambda làm Buffer (Pull Model). <br>&emsp; + Tạo 2 Queue chính: `smart-campus-analytics-queue` và `smart-campus-notification-queue`. <br>&emsp; + Tạo 1 Dead Letter Queue (DLQ) `smart-campus-dlq` chứa message lỗi để kỹ sư kiểm tra. <br>&emsp; + Cấu hình Partial Batch Response để Lambda xử lý từng message độc lập, retry thất bại không ảnh hưởng message thành công. | 13/08/2026 | 13/08/2026 | https://docs.aws.amazon.com/sqs/ |
| 5 | - Nghiên cứu và thiết kế tính năng **Face Liveness Detection**: <br>&emsp; + Vấn đề bảo mật: Nhân viên có thể dùng ảnh/video phát lại để giả mạo điểm danh. <br>&emsp; + Giải pháp: Tích hợp chuẩn AWS Amplify Liveness (Amazon Rekognition Liveness). <br>&emsp; + Thiết kế IAM: Identity Pool (Guest) chỉ cấp quyền `StartFaceLivenessSession`. <br>&emsp; + Thiết kế Backend: `CreateFaceLivenessSession` + `GetFaceLivenessSessionResults`, chặn nếu confidence < 90%. <br>&emsp; + Thiết kế Frontend: SDK `@aws-amplify/ui-react-liveness` – Hiển thị bầu dục, hướng dẫn người dùng điều chỉnh khoảng cách khuôn mặt. | 14/08/2026 | 14/08/2026 | AWS Rekognition Liveness Docs |
| 6 | - Hoàn tất viết **Workshop Documentation** (FCJ Workshop Template): <br>&emsp; + Bài 5.10.2: Kiểm thử Attendance API (Check-in, Face Registration validation, DynamoDB verification). <br>&emsp; + Bài 5.10.4: Kiểm thử hệ thống Giám sát (CloudWatch Logs, X-Ray Service Map, CloudWatch Alarm). <br>&emsp; + Bài 5.10.5: Hướng dẫn dọn dẹp tài nguyên AWS (CloudFront → API Gateway → Lambda → DynamoDB → S3 → Cognito → IAM → Glue). <br> - Viết Báo cáo thu hoạch các sự kiện đã tham dự (Event 1, 2, 3). <br> - Tổng kết Đồ án: Kiến trúc hệ thống hoàn chỉnh, bài học kinh nghiệm, định hướng phát triển tương lai. | 15/08/2026 | 15/08/2026 | FCJ Workshop Template |

### Kết quả đạt được tuần 8:

* Hệ thống Giám sát & Quan sát (Observability) đã hoàn chỉnh:
  * **AWS X-Ray**: Vẽ Service Map trực quan, truy vết toàn bộ request từ API Gateway → Lambda → DynamoDB/S3/Rekognition, đo được latency từng hop trong mili-giây.
  * **CloudWatch Alarm + SNS**: Admin nhận email cảnh báo tự động trong vòng 5 phút khi hệ thống gặp lỗi nghiêm trọng.
* Kiến trúc Message Queue (SQS) tăng cường đáng kể độ tin cậy hệ thống:
  * Không còn mất dữ liệu điểm danh khi có hàng ngàn sinh viên check-in cùng lúc.
  * Dead Letter Queue lưu lại mọi message lỗi để kỹ sư kiểm tra và retry thủ công khi cần.
* Nghiên cứu thành công Face Liveness Detection: Hiểu rõ kiến trúc bảo mật chống Presentation Attack (ảnh, video giả mạo) với Amazon Rekognition Liveness.
* Workshop Documentation hoàn chỉnh với ảnh minh họa chi tiết cho từng bước thực hành, phục vụ cộng đồng học AWS.
* **Đồ án Smart Campus Platform** hoàn thành với đầy đủ:
  * 8 Workflows nghiệp vụ (6/8 đã triển khai đầy đủ, 2/8 đã thiết kế và document).
  * 10+ dịch vụ AWS tích hợp: API Gateway, Lambda, DynamoDB, S3, Rekognition, EventBridge, SNS, SQS, CloudWatch, X-Ray, Cognito, Athena.
  * Kiến trúc Serverless + Event-Driven hoàn chỉnh, có thể mở rộng (scalable) và bảo trì dễ dàng.
