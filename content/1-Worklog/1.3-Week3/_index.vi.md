---
title: "Worklog Tuần 3"
date: 2026-07-07
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

### Mục tiêu tuần 3:

* Xây dựng nền tảng Backend (FastAPI) với 7 modules microservices.
* Khởi tạo giao diện Frontend (React + Vite) với phong cách Glassmorphism cao cấp.
* Tích hợp API thực từ DynamoDB vào Frontend (CRUD Users).
* Thiết lập kết nối hoàn chỉnh giữa Frontend và Backend thông qua REST API.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|-----|-----------|--------------|-----------------|----------------|
| 2 | - Khởi tạo FastAPI server với cấu trúc module hóa (`app/modules/`). <br> - Cấu hình Middleware: CORS (Cross-Origin Resource Sharing) cho phép Frontend kết nối. <br> - Thiết lập hệ thống Error Handler tập trung trả về Error Code chuẩn. <br> - Cấu hình `boto3` kết nối với các dịch vụ AWS (DynamoDB, S3, Rekognition). <br> - Phát triển module `users`: CRUD nhân viên/sinh viên, tìm kiếm theo email, role. | 07/07/2026 | 07/07/2026 | https://fastapi.tiangolo.com/ |
| 3 | - Phát triển các modules Backend còn lại: <br>&emsp; + `faces`: Xử lý ảnh, kết nối Rekognition. <br>&emsp; + `attendance`: Điểm danh, Rule Engine. <br>&emsp; + `notifications`: Gửi thông báo qua SNS. <br>&emsp; + `reports`: Lưu log vào S3 + Athena. <br>&emsp; + `ai_assistant`: Tích hợp Amazon Bedrock. <br> - Định nghĩa Repository layer với `boto3` cho từng module. <br> - Viết các API endpoints cơ bản và test bằng Swagger UI (`/docs`). | 08/07/2026 | 08/07/2026 | https://fastapi.tiangolo.com/ |
| 4 | - Khởi tạo dự án Frontend: `npm create vite@latest` với template React. <br> - Thiết lập CSS Glassmorphism: Dark mode, backdrop-filter blur, transparent background. <br> - Cài đặt thư viện: `lucide-react` (icons), `react-router-dom` (routing). <br> - Xây dựng component layout: `Sidebar`, `Topbar`, `Card`. <br> - Cấu hình React Router với các route cơ bản: `/`, `/users`, `/attendance`. | 09/07/2026 | 09/07/2026 | https://vitejs.dev/ |
| 5 | - Xây dựng trang `Users.jsx`: Bảng danh sách nhân viên với hiệu ứng hover, badge màu theo role. <br> - Tích hợp API thực: Fetch dữ liệu từ bảng `smart-campus-users` DynamoDB lên giao diện. <br> - Xây dựng Modal popup Form thêm User mới (POST API). <br> - Tính năng tự động sinh mã nhân sự theo role: `STU-XXXX`, `MAN-XXXX`, `SEC-XXXX`. <br> - Tính năng chỉnh sửa User (PATCH API): Cập nhật email, role trực tiếp trên web. | 10/07/2026 | 10/07/2026 | React Docs |
| 6 | - Chuẩn hóa dữ liệu Database: Khắc phục không nhất quán tên trường (camelCase → snake_case). <br> - Fix lỗi CORS: Cấu hình đúng `allow_origins`, `allow_methods` trong FastAPI. <br> - Fix bug màu chữ trắng khó nhìn trên Dropdown Select (UX). <br> - Cấu hình Vite Proxy (`/api → http://localhost:8000`) để giải quyết CORS khi dev local. <br> - Test toàn bộ luồng CRUD Users từ Frontend đến DynamoDB. <br> - Viết seed data: Tạo 10 user dummy bao phủ các role và phòng ban. | 11/07/2026 | 11/07/2026 | DynamoDB Docs |

### Kết quả đạt được tuần 3:

* Hoàn thành kiến trúc Backend FastAPI với đầy đủ 7 modules, tất cả có cấu trúc Repository–Service–Router chuẩn.
* Giao diện Frontend React khởi động thành công với phong cách **Glassmorphism** ấn tượng: dark mode, backdrop blur, gradient tinh tế.
* Luồng CRUD Users hoạt động end-to-end:
  * **Tạo mới**: Modal form với auto-generate mã nhân sự.
  * **Hiển thị**: Bảng danh sách real-time từ DynamoDB.
  * **Chỉnh sửa**: Modal edit với kiểm tra email trùng ở Backend.
* Giải quyết triệt để vấn đề CORS giữa Frontend (port 5173) và Backend (port 8000) thông qua Vite Proxy.
* Chuẩn hóa toàn bộ schema DynamoDB về `snake_case`, tạo nền tảng nhất quán cho các module sau.
* 10 tài khoản seed data được tạo, sẵn sàng cho việc kiểm thử phân quyền (RBAC) ở các tuần tiếp theo.
