---
title: "Worklog Tuần 6"
date: 2026-07-28
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Mục tiêu tuần 6:

* Tích hợp hoàn chỉnh AWS Cognito cho xác thực 2 lớp, đăng nhập sinh trắc học và quản lý mật khẩu an toàn.
* Tái thiết kế trang Analytics với RBAC 3 tầng và giao diện SVG Donut Chart cao cấp.
* Hoàn thiện tính năng đăng nhập / khôi phục mật khẩu bằng khuôn mặt.

### Các công việc cần triển khai trong tuần này:

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
|-----|-----------|--------------|-----------------|----------------|
| 2 | - Tích hợp AWS Cognito (WF1 – Authentication): <br>&emsp; + Tích hợp `admin_create_user` (Cognito Boto3) vào endpoint tạo tài khoản của Admin. <br>&emsp; + AWS Cognito tự động sinh Temporary Password và gửi qua Email nhân sự mới (tích hợp sẵn, không cần SES). <br>&emsp; + Mở rộng module Auth: Thêm API `POST /api/auth/respond-challenge` để bắt tín hiệu `NEW_PASSWORD_REQUIRED`. <br>&emsp; + Frontend `Login.jsx`: Nếu đăng nhập bằng mật khẩu tạm → Chuyển sang giao diện "Đặt mật khẩu mới". | 28/07/2026 | 28/07/2026 | https://docs.aws.amazon.com/cognito/ |
| 3 | - Hoàn thiện Luồng sinh trắc học nâng cao: <br>&emsp; + Trang **My Profile**: Nhân viên tự đăng ký khuôn mặt không qua Admin (Webcam + Upload). <br>&emsp; + Chống duplicate: Tích hợp `SearchFacesByImage` trước `IndexFaces` → Chặn nếu khuôn mặt đã tồn tại. <br>&emsp; + **Đăng nhập bằng khuôn mặt**: Nhân viên quét khuôn mặt → Backend SearchFaces → Trả JWT token. <br>&emsp; + **Khôi phục mật khẩu bằng khuôn mặt**: Xác thực danh tính bằng FaceID → Đặt lại mật khẩu mới. <br> - Fix bug Camera UI: Rò rỉ bộ nhớ khi chuyển tab, cập nhật `stopFaceCamera()` giải phóng luồng video. | 29/07/2026 | 29/07/2026 | AWS Rekognition Docs |
| 4 | - Tái thiết kế Dashboard: Xóa `Dashboard.jsx` cũ, thay trang chủ `/` bằng trang `Analytics.jsx`. <br> - Tái thiết kế UX/UI trang Analytics (Premium Glassmorphism): <br>&emsp; + KPI Cards với **Circular Progress Ring (SVG)** hiển thị tỉ lệ chuyên cần dạng vòng tròn. <br>&emsp; + Area Chart tối ưu: Gradient Cyan (Có mặt) và Amber (Đi muộn). <br>&emsp; + **Task Overview** bằng **SVG Donut Chart thuần** (không dùng thư viện): Trực quan hóa trạng thái Tasks. <br>&emsp; + Top nhân viên vắng mặt: List view + Horizontal Progress Bar (Xanh >90%, Vàng >70%, Đỏ <70%). | 30/07/2026 | 30/07/2026 | React / SVG Docs |
| 5 | - Tích hợp **RBAC 3 tầng** vào trang Analytics (không cần thay đổi Backend): <br>&emsp; + **Tầng 1 (ADMIN/DIRECTOR)**: Toàn hệ thống + Bảng so sánh hiệu suất giữa các Phòng ban. <br>&emsp; + **Tầng 2 (MANAGER)**: Bộ lọc khóa theo phòng ban của mình. <br>&emsp; + **Tầng 3 (STAFF)**: Chuyển thành "My Analytics" – chỉ dữ liệu cá nhân. <br> - Fix bug 500 API Notifications: Thay `Query` bằng `Scan` + `FilterExpression` làm fallback an toàn khi GSI chưa tạo. | 31/07/2026 | 31/07/2026 | DynamoDB Docs |
| 6 | - Fix bug 500 khi đổi mật khẩu: Map đúng `InvalidPasswordException` → `VALIDATION_ERROR` (422). <br> - Hợp nhất Tasks: Gộp trang "My Tasks" vào "Tasks" tổng, loại bỏ dư thừa. <br> - Tối ưu UX Notifications: Xóa cột "Trạng thái", fix chấm đỏ Unread tự tắt khi hover chuông. <br> - Cập nhật logic gọi API: Mỗi nhân viên chỉ thấy thông báo của chính mình (bảo vệ quyền riêng tư). <br> - Test toàn bộ luồng Cognito: Tạo tài khoản → Nhận email tạm → Đăng nhập → Force change password. | 01/08/2026 | 01/08/2026 | AWS Cognito Docs |

### Kết quả đạt được tuần 6:

* Hệ thống xác thực AWS Cognito hoàn chỉnh:
  * Admin tạo tài khoản → Nhân sự nhận email với mật khẩu tạm → Đăng nhập lần đầu buộc phải đổi mật khẩu mới.
  * Mật khẩu phải đáp ứng độ phức tạp: Ít nhất 8 ký tự, chữ hoa, thường, số, ký tự đặc biệt.
* Đăng nhập sinh trắc học hoàn chỉnh:
  * Nhân viên có thể đăng nhập bằng khuôn mặt, không cần nhập mật khẩu.
  * Khôi phục mật khẩu bằng khuôn mặt – tính năng tiên tiến không cần OTP hay SES.
* Trang Analytics mới cao cấp hơn hẳn:
  * SVG Donut Chart tự xây dựng không phụ thuộc thư viện ngoài.
  * Circular Progress Ring hiệu ứng đẹp mắt.
  * RBAC 3 tầng hoàn toàn bằng Frontend logic, không cần thay đổi Backend.
* Chống gian lận đăng ký khuôn mặt: Một khuôn mặt chỉ được đăng ký cho một tài khoản.
