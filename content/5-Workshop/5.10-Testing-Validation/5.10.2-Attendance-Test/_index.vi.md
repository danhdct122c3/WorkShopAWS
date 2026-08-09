---
title : "Kiểm thử điểm danh"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.10.2. </b> "
---

#### Kiểm thử luồng điểm danh nhận diện khuôn mặt qua giao diện Web

Đây là luồng nghiệp vụ cốt lõi của hệ thống: Đăng ký khuôn mặt vào Rekognition, sau đó gửi ảnh để nhận diện và ghi nhận điểm danh vào DynamoDB. Thay vì dùng Postman, chúng ta sẽ trải nghiệm trực tiếp trên giao diện Frontend của ứng dụng.

---

**Bước 1: Đăng nhập vào trang web**

1. Mở trang web Frontend của bạn (URL của CloudFront hoặc chạy local qua `npm run dev`).
2. Đăng nhập bằng tài khoản vừa tạo ở phần trước.
3. Chuyển sang menu **Điểm danh (Attendance)**.

---

**Bước 2: Đăng ký khuôn mặt lần đầu**

Vì đây là lần đầu tiên tài khoản này sử dụng hệ thống, ứng dụng sẽ yêu cầu bạn đăng ký khuôn mặt.

1. Tại trang Điểm danh, bạn sẽ thấy thông báo **Tài khoản của bạn chưa có khuôn mặt**.
2. Nhấn nút **Bật Camera** và cho phép trình duyệt truy cập Webcam.
3. Ngồi thẳng, đảm bảo mặt rõ nét trong khung hình và nhấn nút **Chụp ảnh & Đăng ký khuôn mặt**.
4. Chờ hệ thống gọi API `POST /api/faces/register`.

> **Kết quả mong đợi:** Nhận được thông báo "Đăng ký khuôn mặt thành công!". Trạng thái tài khoản của bạn đã được cập nhật thành đã có khuôn mặt.

---

**Bước 3: Xác thực ảnh đã lưu trên S3**

1. Vào AWS Console > **S3** > Bucket `smart-campus-images-{id}`.
2. Mở thư mục `face/`.
3. Bạn sẽ thấy file ảnh vừa chụp bằng Webcam được lưu với định dạng `{user_id}/{face_id}.jpg`.

> **Kết quả mong đợi:** File ảnh tồn tại trong S3, có thể preview được chính xác ảnh bạn vừa chụp.

---

**Bước 4: Thực hiện Check-in (Điểm danh)**

Sau khi đã đăng ký khuôn mặt, giao diện Điểm danh sẽ chuyển sang chế độ Check-in.

1. Nhấn nút **Bật Camera** (nếu camera đang tắt).
2. Nhấn nút **Chụp ảnh (Check in)**.
3. Hệ thống sẽ gọi API `POST /api/attendance/recognize` để đối chiếu với ảnh gốc trong Rekognition.

> **Kết quả mong đợi:** Có thông báo "Điểm danh thành công!", màn hình hiển thị tên, phòng ban và độ tin cậy (Confidence) của khuôn mặt. Đồng thời, một bản ghi điểm danh mới xuất hiện trong bảng "Lịch sử điểm danh hôm nay".

---

**Bước 5: Xác thực bản ghi trong DynamoDB**

1. Vào AWS Console > **DynamoDB** > Tables > `smart-campus-attendance`.
2. Bấm nút **Explore table items**.
3. Bạn sẽ thấy bản ghi mới xuất hiện với các trường: `record_id`, `user_id`, `date`, `timestamp`, `status`.

> **Kết quả mong đợi:** Bản ghi điểm danh vừa thực hiện đã được ghi vào DynamoDB.

---

**Bước 6: Kiểm thử trường hợp nhận diện thất bại (Negative Test)**

Để đảm bảo hệ thống xử lý đúng, hãy thử:
1. Nhờ một người khác (không phải bạn) ngồi vào trước Camera và nhấn Check in.
2. Hoặc đưa một vật dụng (điện thoại, cốc nước) che mặt hoặc không có mặt người và nhấn Check in.

> **Kết quả mong đợi:** Hệ thống báo lỗi không nhận diện được hoặc không tìm thấy khuôn mặt trùng khớp.

