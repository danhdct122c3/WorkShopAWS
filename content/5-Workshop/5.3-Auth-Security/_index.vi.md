---
title : "Cấu hình Xác thực & Bảo mật"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

### Mục tiêu (Goal)

Trong phần này, chúng ta sẽ xây dựng tuyến phòng thủ xác thực người dùng đầu tiên cho toàn bộ hệ thống Smart Campus. Thay vì phải tự code logic mã hóa mật khẩu và tạo Token phức tạp, chúng ta sẽ ủy thác hoàn toàn cho **Amazon Cognito**.

> [!NOTE]
> **AWS WAF** (bảo vệ API khỏi truy cập trái phép từ bên ngoài Campus) sẽ được cấu hình ở **mục 5.5.4** — sau khi API Gateway và Lambda đã được tạo xong, vì WAF cần Invoke URL của API Gateway để hoạt động.

### Các nội dung thực hành chi tiết

Vui lòng bấm chọn từng mục dưới đây ở thanh menu bên trái hoặc click trực tiếp vào các liên kết dưới đây để thực hiện chi tiết từng bước:

{{% children /%}}
