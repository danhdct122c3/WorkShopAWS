---
title: "Tuần 4: Xây dựng Core API & Rule Engine"
date: 2026-06-22
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---





## 1. Mục tiêu công việc
Hoàn thành CRUD cho Users, Tasks. Viết Rule Engine tính toán logic Điểm danh trễ/đúng giờ dựa trên bảng Settings.

## 2. Nhật ký công việc chi tiết

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|---|---|---|---|---|
| 2 | - Thiết lập S3 Bucket (Block Public Access) và viết lớp wrapper `rekognition.py`.<br>- Tích hợp các hàm `IndexFaces` và `SearchFacesByImage` vào Backend. | 13/07/2026 | 13/07/2026 | https://docs.aws.amazon.com/ |
| 3 | - Hoàn thành API đăng ký khuôn mặt (nhận ảnh base64, decode, validate).<br>- Xử lý lưu ảnh gốc lên S3 và gọi IndexFaces để sinh `faceId` lưu vào DynamoDB. | 14/07/2026 | 14/07/2026 | https://cloudjourney.awsstudygroup.com/ |
| 4 | - Xây dựng Rule Engine điểm danh với 3 ca làm việc (Morning, Afternoon, Evening).<br>- Cài đặt logic tự động phân loại trạng thái điểm danh (PRESENT, LATE, REJECTED). | 15/07/2026 | 15/07/2026 | https://docs.aws.amazon.com/ |
| 5 | - Tối ưu truy vấn bằng cách tạo thêm GSI `date-index`, `userid-index` trên DynamoDB.<br>- Áp dụng cơ chế Idempotency chống điểm danh trùng lặp trong cùng một ca. | 16/07/2026 | 16/07/2026 | https://cloudjourney.awsstudygroup.com/ |
| 6 | - Cấu hình đẩy sự kiện `AttendanceRecorded`, `AttendanceRejected` lên EventBridge.<br>- Xử lý lỗi boto3 không hỗ trợ Float bằng cách parse BoundingBox sang String. | 17/07/2026 | 17/07/2026 | https://docs.aws.amazon.com/ |



## 3. Các kết quả đạt được
- Hoàn thành luồng đăng ký khuôn mặt và Rule Engine điểm danh thông minh, tích hợp thành công Rekognition & EventBridge.
