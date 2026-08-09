---
title : "Kiểm thử (Testing & Validation)"
date : 2024-01-01
weight : 10
chapter : false
pre : " <b> 5.10. </b> "
---

### Mục tiêu (Goal)

Để đảm bảo hệ thống Smart Campus đáp ứng được các tiêu chuẩn chấm điểm và hoạt động đúng thiết kế, chúng ta cần thực hiện quy trình kiểm thử End-to-End. Phần này hướng dẫn bạn cách kích hoạt luồng hệ thống và xác thực kết quả ở từng dịch vụ AWS.

#### 1. Kiểm thử gửi Request (Postman / Frontend)
1. Lấy URL của API Gateway (Ví dụ: `https://xyz.execute-api.ap-southeast-1.amazonaws.com/prod/attendance`).
2. Mở Postman, chọn phương thức **POST**. Dán URL vào.
3. Ở tab **Body** > **raw** > **JSON**, nhập payload chứa ảnh khuôn mặt sinh viên (base64) và `camera_id`.
4. Bấm **Send**.
5. Nhận lại kết quả `200 OK` với thông điệp: "Điểm danh thành công cho sinh viên ...".

#### 2. Xác thực lưu trữ tại DynamoDB & S3
1. **DynamoDB:** Truy cập AWS Console > DynamoDB > Tables > `smart-campus-attendance`.
   - Bấm **Explore table items**.
   - Bạn sẽ thấy một bản ghi mới xuất hiện với `attendance_id`, thời gian và trạng thái đi học.
2. **S3 (Image Storage):** Truy cập S3 bucket `smart-campus-images`.
   - Kiểm tra xem file ảnh khuôn mặt vừa gửi lên có được lưu lại với định dạng tên `YYYY-MM-DD/ID.jpg` hay không.

#### 3. Xác thực Log & Metric (CloudWatch)
1. Truy cập CloudWatch > Log groups > Chọn log group của Lambda `smart-campus-api`.
2. Kiểm tra log stream mới nhất để xem các dòng lệnh `print` thời gian thực thi, kết quả trả về từ Amazon Rekognition.
3. Chuyển sang phần **Metrics**, chọn hàm Lambda và kiểm tra biểu đồ **Invocations** (Số lượt gọi) xem cột biểu đồ có nhích lên 1 đơn vị không.

#### 4. Xác thực Event-Driven (SNS / SQS)
1. Mở Hòm thư (Gmail) mà bạn đã đăng ký với SNS ở Bước 5.6.
2. Bạn sẽ nhận được một Email mới từ AWS báo cáo sự kiện điểm danh.
3. Nếu bạn có cấu hình SQS, hãy truy cập SQS > Chọn `smart-campus-analytics-queue` > Bấm **Send and receive messages** > **Poll for messages** để xem sự kiện định tuyến từ EventBridge đã được đẩy vào hàng đợi chưa.

Nếu tất cả các bước trên đều trả về kết quả đúng như kỳ vọng, xin chúc mừng! Bạn đã triển khai thành công 100% kiến trúc Serverless Event-Driven trên AWS.
