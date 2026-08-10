---
title : "Chuẩn bị tài nguyên"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

Để bắt đầu triển khai hệ thống **Smart Campus Platform**, bạn cần chuẩn bị các công cụ và tài nguyên cơ bản trên môi trường AWS.

### 1. Tài khoản AWS (AWS Account)
- Bạn cần một tài khoản AWS với quyền quản trị viên (`AdministratorAccess`).
- Nếu bạn sử dụng tài khoản mới tạo (Free Tier), hệ thống Serverless này được thiết kế để hoàn toàn nằm trong giới hạn miễn phí của AWS, đảm bảo bạn không phát sinh chi phí trong quá trình thực hành.
- **Region khuyên dùng:** Chọn khu vực `ap-southeast-1` (Singapore) để có độ trễ thấp nhất về Việt Nam.

### 2. Chuẩn bị IAM Role cơ bản
Trong hệ thống này, các dịch vụ AWS cần giao tiếp với nhau (Ví dụ: Lambda gọi Rekognition, API Gateway gọi Lambda). Để đảm bảo nguyên tắc **Đặc quyền tối thiểu (Least Privilege)**, chúng ta sẽ tạo các IAM Role cụ thể ở từng bước thực hành. Tuy nhiên, trước mắt bạn cần hiểu nguyên tắc:
- Không sử dụng Access Key / Secret Key nhúng cứng (hard-code) vào code.
- Tất cả quyền giao tiếp đều được cấp phát qua **IAM Role**.

### 3. Cài đặt các công cụ (Tools) tại máy tính nội bộ
Mặc dù bạn có thể cấu hình toàn bộ hệ thống bằng giao diện (AWS Console), việc cài đặt các công cụ dưới đây sẽ giúp bạn test API và quản lý source code dễ dàng hơn:
- **Visual Studio Code (VSCode):** Để đọc và chỉnh sửa mã nguồn Frontend (React) và Backend (Python/FastAPI).
- **Postman** : Dùng để test các API Endpoint mà chúng ta sắp tạo trên Amazon API Gateway.
- **Git:** Cần thiết để push source code lên kho lưu trữ và tích hợp với AWS CodePipeline sau này.

### 4. Source Code dự án
Vui lòng clone (tải về) mã nguồn chuẩn của dự án Smart Campus về máy tính cá nhân của bạn để sử dụng cho các bước tiếp theo:

```bash
git clone https://github.com/your-username/smart-campus-serverless.git
cd smart-campus-serverless
```
*(Cấu trúc thư mục source code sẽ bao gồm 2 phần chính: `/frontend` chứa code ReactJS và `/backend` chứa code Python cho Lambda).*

---
Sau khi đã chuẩn bị xong, hãy chuyển sang bài tiếp theo để bắt đầu **Phần 1: Thiết lập Xác thực & Bảo mật đa lớp**.