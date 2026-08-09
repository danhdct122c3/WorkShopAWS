---
title : "Tạo S3 Bucket Hosting"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.8.1. </b> "
---

#### Hosting Frontend trên Amazon S3
Amazon S3 có một tính năng vô cùng lợi hại là **Static Website Hosting**. Bạn chỉ việc upload các file HTML, CSS, JS (sau khi đã build) lên S3, nó sẽ biến thành một máy chủ web thực thụ mà không cần bạn phải duy trì hệ điều hành hay phần mềm web server (như Nginx/Apache).

**Bước 1: Tạo S3 Bucket cho Website**

1. Từ thanh tìm kiếm AWS Console, mở dịch vụ **S3**.
2. Bấm **Create bucket**.
3. **Bucket name**: Đặt tên có ý nghĩa, ví dụ `smart-campus-frontend-2024` (Lưu ý: Tên bucket phải là duy nhất trên toàn cầu AWS).
> ![Tạo S3 Bucket](/aws-image/setupS3frontend/s31.png)
4. Ở phần **Object Ownership**, chọn **ACLs disabled (recommended)**.
> ![Object Ownership](/aws-image/setupS3frontend/s32.png)
5. Ở phần **Block Public Access settings for this bucket**:
   - Bỏ chọn **Block all public access** (nếu bạn muốn public ngay bây giờ) hoặc giữ nguyên nếu dùng CloudFront. Trong xưởng này chúng ta bỏ chọn để test độc lập.
> ![Block Public Access](/aws-image/setupS3frontend/s33_1.png)
6. Đánh dấu xác nhận (Acknowledge) cảnh báo của AWS.
> ![Xác nhận cảnh báo](/aws-image/setupS3frontend/s33_2.png)
7. Cuộn xuống cuối và bấm **Create bucket**.
> ![Tạo bucket thành công](/aws-image/setupS3frontend/s33_3.png)

**Bước 2: Bật Static Website Hosting**

1. Vào bucket vừa tạo, chuyển sang tab **Properties**.
> ![Tab Properties](/aws-image/setupS3frontend/s34_1.png)
2. Cuộn xuống cuối cùng đến phần **Static website hosting**, bấm **Edit**. Chọn **Enable**. Ở mục **Index document**, điền `index.html`. Bấm **Save changes**.
> ![Cấu hình Index Document](/aws-image/setupS3frontend/s34_2.png)
3. Cấu hình hoàn tất, bạn sẽ nhận được một đường link URL tĩnh (Endpoint) ở dưới cùng.
> ![Static website endpoint](/aws-image/setupS3frontend/s34_3.png)

**Bước 3: Upload source code và cấu hình Policy**

1. Bấm vào tab **Objects** và chọn **Upload**. Kéo thả các file trong thư mục build của React/Vue vào.
> ![Upload files](/aws-image/setupS3frontend/s35.png)
2. Chuyển sang tab **Permissions**. Cuộn đến phần **Bucket policy** và bấm **Edit**.
> ![Tab Permissions](/aws-image/setupS3frontend/s36.png)
3. Điền cấu hình Policy dạng JSON để cho phép `s3:GetObject` công khai. Bấm **Save changes**.
> ![Cấu hình Policy](/aws-image/setupS3frontend/s36_2.png)
4. Quay lại tab Properties, click vào link Static website endpoint vừa nhận được ở Bước 2.
> ![Click endpoint](/aws-image/setupS3frontend/s37.png)
5. Chờ trình duyệt tải, bạn sẽ thấy giao diện Frontend hiện ra thành công!
> ![Giao diện Frontend 1](/aws-image/setupS3frontend/s38_1.png)
6. Xin chúc mừng, ứng dụng Frontend Smart Campus của bạn đã chính thức chạy trên mây.
> ![Giao diện Frontend 2](/aws-image/setupS3frontend/s38_2.png)
