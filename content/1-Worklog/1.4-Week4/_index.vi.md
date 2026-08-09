---
title: "Worklog Tuần 4"
date: 2026-07-14
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu tuần 4:

* Tích hợp hoàn chỉnh hệ thống nhận diện khuôn mặt bằng Amazon Rekognition & S3.
* Xây dựng luồng nghiệp vụ Điểm danh (WF3) với Rule Engine tự động phân loại trạng thái.
* Đảm bảo tính toàn vẹn dữ liệu và chống gian lận điểm danh trùng.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|-----|-----------|--------------|-----------------|----------------|
| 2 | - Nghiên cứu chuyên sâu AWS Rekognition: Cơ chế `IndexFaces` và `SearchFacesByImage`. <br> - Thiết lập S3 Bucket `smart-campus-images` với cấu hình Block Public Access. <br> - Cấu hình CORS cho S3 Bucket để cho phép Frontend upload trực tiếp. <br> - Tạo Rekognition Collection `smart-campus-faces` để lập chỉ mục khuôn mặt. <br> - Viết hàm wrapper `rekognition.py` trong Backend (IndexFaces, SearchFacesByImage). | 14/07/2026 | 14/07/2026 | https://docs.aws.amazon.com/rekognition/ |
| 3 | - Phát triển luồng **WF2 – Đăng ký khuôn mặt (Face Registration)** End-to-End: <br>&emsp; + **Frontend**: Thêm Modal "Đăng ký khuôn mặt" trên trang `Users.jsx`. <br>&emsp; + Hỗ trợ 2 phương thức: Upload file ảnh có sẵn hoặc bật Webcam chụp trực tiếp (`navigator.mediaDevices`). <br>&emsp; + **Backend**: Nhận ảnh base64, decode, validate (JPEG/PNG, tối đa 5MB). <br>&emsp; + Gọi API lưu ảnh gốc lên S3. <br>&emsp; + Tích hợp `IndexFaces` để tạo `faceId`, `confidence`, `BoundingBox`. | 15/07/2026 | 15/07/2026 | https://docs.aws.amazon.com/rekognition/ |
| 4 | - Fix lỗi DynamoDB: Boto3 không hỗ trợ kiểu `Float` từ Rekognition → parse BoundingBox sang `String`. <br> - Đồng bộ tên Partition Key: `faceId` → `face_id` chuẩn theo schema. <br> - Fix lỗi CORS Policy trong `main.py` khi Backend phát sinh exception. <br> - Phát triển luồng **WF3 – Điểm danh (Attendance)**: <br>&emsp; + Rule Engine định nghĩa 3 ca học: `MORNING` (7:00–12:00), `AFTERNOON` (13:00–17:30), `EVENING` (17:30–21:00). <br>&emsp; + Phân loại tự động: `PRESENT` (đúng giờ), `LATE` (muộn 15 phút), `REJECTED` (trùng lặp/ngoài ca). | 16/07/2026 | 16/07/2026 | DynamoDB Docs / FastAPI Docs |
| 5 | - Xây dựng module `attendance` Backend: <br>&emsp; + Repository với GSI `date-index`, `userid-index` hỗ trợ truy vấn nhanh. <br>&emsp; + Service tích hợp `SearchFacesByImage` từ Rekognition, gọi Rule Engine, lưu DynamoDB. <br>&emsp; + Publish event `AttendanceRecorded` / `AttendanceRejected` / `UnknownFaceDetected` lên EventBridge. <br> - Cơ chế **Idempotency**: Kiểm tra xem người dùng đã điểm danh trong ca hiện tại chưa, nếu rồi thì `REJECTED`. | 17/07/2026 | 17/07/2026 | AWS EventBridge Docs |
| 6 | - Xây dựng trang `Attendance.jsx` (Frontend): <br>&emsp; + Giao diện bật Webcam, chụp ảnh và gửi lên Backend để nhận diện. <br>&emsp; + Hiển thị kết quả nhận diện: Tên nhân viên, mức độ tin cậy (confidence %), trạng thái điểm danh. <br>&emsp; + Bảng lịch sử điểm danh với filter theo ngày và ca học. <br>&emsp; + Badge trạng thái màu sắc trực quan: Xanh (PRESENT), Vàng (LATE), Đỏ (REJECTED). <br> - Test toàn bộ luồng WF2 → WF3 end-to-end. | 18/07/2026 | 18/07/2026 | React Docs |

### Kết quả đạt được tuần 4:

* Luồng WF2 (Đăng ký khuôn mặt) hoàn chỉnh end-to-end:
  * Nhân viên có thể Upload ảnh hoặc bật Webcam chụp trực tiếp ngay trên trình duyệt.
  * Ảnh được lưu S3, khuôn mặt được index vào Rekognition Collection với đầy đủ metadata.
* Luồng WF3 (Điểm danh) hoàn chỉnh với Rule Engine thông minh:
  * Phân loại chính xác PRESENT / LATE / REJECTED dựa trên thời gian thực.
  * Cơ chế Idempotency ngăn điểm danh trùng lặp trong cùng ca học.
  * Sự kiện điểm danh tự động publish lên EventBridge để các module khác xử lý tiếp.
* Khắc phục các lỗi kỹ thuật quan trọng:
  * Bug Boto3 Float từ Rekognition: Đã parse về String trước khi lưu DynamoDB.
  * Bug CORS Policy: Backend không báo lỗi giả khi phát sinh exception.
* Hiểu sâu hơn về AWS Rekognition: Sự khác biệt giữa Collection (lưu vector khuôn mặt) và S3 (lưu ảnh thực).
