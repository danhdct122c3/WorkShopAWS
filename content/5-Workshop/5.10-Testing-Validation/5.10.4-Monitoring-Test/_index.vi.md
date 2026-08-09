---
title : "Kiểm thử giám sát"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 5.10.4. </b> "
---

#### Kiểm thử Log, Metric và Tracing (CloudWatch & X-Ray)

Phần này hướng dẫn bạn xem log thời gian thực, kiểm tra metric và phân tích luồng request qua X-Ray để xác nhận hệ thống giám sát đang hoạt động đúng.

---

**Bước 1: Xem Log Lambda trên CloudWatch**

1. Vào AWS Console > **CloudWatch** > **Log groups**.
2. Tìm và chọn log group có tên `/aws/lambda/smart-campus-api`.
3. Bấm vào **Log stream** mới nhất (thường là stream có tên dài với timestamp gần nhất).
4. Bạn sẽ thấy các dòng log chi tiết cho từng lần gọi API, bao gồm:
   - Thời gian bắt đầu và kết thúc request
   - Kết quả trả về từ Rekognition
   - Thông tin bản ghi được ghi vào DynamoDB
   - Sự kiện được phát lên EventBridge

> **Kết quả mong đợi:** Log hiển thị rõ ràng các bước xử lý, không có dòng `ERROR` hoặc `Exception`.

---

**Bước 2: Kiểm tra Metric Lambda**

1. Vào **CloudWatch** > **Metrics** > **All metrics**.
2. Chọn namespace **AWS/Lambda**.
3. Chọn dimension **By Function Name** > Chọn `smart-campus-api`.
4. Thêm các metric cần theo dõi:
   - **Invocations**: Số lượt gọi hàm (phải tăng tương ứng số lần bạn test)
   - **Duration**: Thời gian xử lý trung bình (ms)
   - **Errors**: Số lượt lỗi (kỳ vọng là 0)
5. Chọn khoảng thời gian **Last 1 hour** và quan sát biểu đồ.

> **Kết quả mong đợi:** Metric Invocations tăng, Errors = 0, Duration dưới 3000ms (3 giây).

---

**Bước 3: Phân tích Trace trên X-Ray**

1. Vào **CloudWatch** > **X-Ray traces** > **Service map** (hoặc truy cập trực tiếp dịch vụ **X-Ray** trên Console).
2. Chọn khoảng thời gian **Last 30 minutes**.
3. Bạn sẽ thấy bản đồ dịch vụ với các node: `Client` → `smart-campus-api (Lambda)` → `DynamoDB`, `Rekognition`, `S3`, `EventBridge`.
4. Bấm vào node **Lambda** để xem chi tiết latency.
5. Chuyển sang **Traces**, chọn một trace cụ thể để xem biểu đồ thác nước (waterfall) thể hiện thời gian từng bước xử lý.

> **Kết quả mong đợi:** Tất cả segment trong trace đều có màu xanh (thành công), không có segment màu đỏ (lỗi).

---

**Bước 4: Kích hoạt CloudWatch Alarm (Kiểm thử Alert)**

Để chứng minh Alarm hoạt động, bạn có thể chủ động gây ra lỗi để Alarm kích hoạt:

1. Gọi API điểm danh với một ảnh không chứa khuôn mặt (ảnh phong cảnh) vài lần liên tiếp.
2. Vào **CloudWatch** > **Alarms** > Chọn alarm `Lambda-Error-Alert`.
3. Sau khoảng 5 phút (1 chu kỳ đánh giá), trạng thái Alarm sẽ chuyển từ `OK` → `In alarm`.
4. Đồng thời, bạn sẽ nhận được Email cảnh báo từ SNS Topic `smart-campus-notifications`.

> **Kết quả mong đợi:** Alarm chuyển trạng thái và Email cảnh báo được gửi đến hộp thư của bạn.
