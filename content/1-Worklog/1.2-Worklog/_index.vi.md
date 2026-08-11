---
title: "Member 2 - Backend"
date: 2026-06-22
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

# Nhật Ký Công Việc: Backend Developer (Member 2)

**Vai trò:** Phát triển Core API bằng Python/FastAPI, thiết kế Cơ sở dữ liệu và Tích hợp hệ thống xác thực.

## Tổng Kết Đóng Góp (Summary)
Trong suốt 8 tuần, tôi chịu trách nhiệm chính trong việc xây dựng "bộ não" của hệ thống **Smart Campus**. Thay vì dùng các framework nặng nề (như Spring Boot hay Django) chạy trên máy chủ ảo (EC2), tôi đã triển khai kiến trúc 100% **Serverless** bằng cách đóng gói **FastAPI** chạy trực tiếp trên **AWS Lambda** thông qua **API Gateway**. Cách tiếp cận này giúp dự án khởi động cực nhanh (Cold start thấp) và chi phí bằng 0 khi không có ai truy cập.

Dưới đây là nhật ký chi tiết:

## Tuần 1-2: Thiết kế Database & Khởi tạo API
**Nội dung công việc:**
- Thiết kế mô hình NoSQL trên **Amazon DynamoDB**. Phân tích kỹ thuật truy cập dữ liệu để tạo ra 5 bảng chính (`Users`, `Attendance`, `Tasks`, `Leaves`, `Settings`).
- Khởi tạo project Python sử dụng framework **FastAPI**.
- Cấu hình thư viện `boto3` để kết nối mã nguồn với DynamoDB.
- **Khó khăn:** DynamoDB không hỗ trợ `JOIN` như SQL thông thường, gây khó khăn khi lấy danh sách Công việc (Tasks) kèm theo tên của Nhân viên (Users).
- **Giải pháp:** Áp dụng kỹ thuật Denormalization (chuẩn hóa ngược) - lưu sẵn `user_name` vào thẳng bảng `Tasks`, đồng thời cấu hình **Global Secondary Index (GSI)** để truy vấn siêu tốc theo `assignee_id`.

## Tuần 3: Xây dựng Core API (CRUD Modules)
**Nội dung công việc:**
- Viết API cho Module Quản lý Nhân sự (`POST /users`, `GET /users`, v.v.).
- Chuẩn hóa cấu trúc mã nguồn theo mô hình 3 lớp: `Router` (Tiếp nhận request) -> `Service` (Xử lý nghiệp vụ) -> `Repository` (Tương tác Database).
- **Refactoring:** Chuyển đổi toàn bộ chuẩn dữ liệu từ `camelCase` sang `snake_case` ở phía Backend để code Python chuẩn Pythonic (PEP 8). Cấu hình FastAPI tự động parse về `camelCase` khi trả response cho Frontend.

## Tuần 4-5: Nghiệp vụ phức tạp (Rule Engine & Presigned URL)
**Nội dung công việc:**
- Xây dựng **Rule Engine** cho module Điểm danh: So sánh thời gian check-in của nhân viên với Giờ làm việc chuẩn trong bảng `Settings` để tự động gán trạng thái `LATE` (Đi trễ) hay `PRESENT` (Đúng giờ).
- Viết API cấp phép upload file (`/tasks/presigned-url`). API này gọi AWS S3 SDK tạo ra một đường link tạm thời (15 phút) trả về cho Frontend, hỗ trợ upload báo cáo dung lượng lớn (50MB) an toàn.

## Tuần 6: Tích hợp Xác thực Đa lớp (Amazon Cognito & JWT)
**Nội dung công việc:**
- Tạo **Amazon Cognito User Pool** trên AWS Console.
- Viết lớp bảo vệ API (`dependencies.py`): Mọi request gửi tới Backend đều phải chứa JWT Token. 
- Lambda sẽ fetch bộ Public Key (JWKS) từ Cognito về để giải mã và kiểm tra chữ ký (Signature) của Token. Nếu hợp lệ mới cho phép truy cập DB.
- Cài đặt hệ thống phân quyền (RBAC): Chỉ `ADMIN` mới được phép xóa User, `MANAGER` được duyệt đơn, `STAFF` chỉ xem thông tin cá nhân.

## Tuần 7-8: AWS API Gateway, Logging & CI/CD
**Nội dung công việc:**
- Đóng gói toàn bộ code FastAPI thông qua thư viện `Mangum`.
- Tích hợp hàm Lambda với **Amazon API Gateway** (Sử dụng HTTP API/REST API Proxy Integration).
- Gắn thêm CORS middleware để Frontend (chạy trên domain khác) có thể gọi được API mà không bị chặn.
- Thiết lập `AWS CodeBuild` tự động chạy Unit Tests (`pytest`) và đóng gói mã nguồn thành file `.zip`, sau đó tự động update phiên bản mới lên AWS Lambda (`aws lambda update-function-code`).
