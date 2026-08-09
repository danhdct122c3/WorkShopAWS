---
title : "Triển khai & Tự động hóa CI/CD"
date : 2024-01-01
weight : 8
chapter : false
pre : " <b> 5.8. </b> "
---

### Mục tiêu (Goal)

Đến thời điểm hiện tại, Back-end API (Serverless) của Smart Campus đã hoạt động trơn tru. Bây giờ là lúc chúng ta đưa Giao diện người dùng (Front-end) lên Cloud, đồng thời thiết lập luồng tích hợp và triển khai liên tục (CI/CD) cho cả Frontend và Backend để tự động hóa hoàn toàn vòng đời phát triển phần mềm.

Trong chương này chúng ta sẽ thực hiện:
1. **Host trang web tĩnh trên Amazon S3:** Rẻ, bền bỉ và không cần quản lý máy chủ.
2. **Tăng tốc với Amazon CloudFront (CDN):** Cache nội dung ở các Edge Location trên toàn cầu, giúp tải trang web cực nhanh và tăng cường bảo mật (cung cấp sẵn SSL/TLS HTTPS).
3. **Tự động hóa luồng CI/CD cho Frontend & Backend với AWS CodePipeline:** Thay vì mỗi lần code xong phải build thủ công và gõ lệnh deploy, chúng ta sẽ thiết lập một luồng CI/CD (Continuous Integration / Continuous Deployment). Cứ mỗi khi lập trình viên đẩy code lên GitHub, AWS sẽ tự động kéo code về, Build và Deploy phiên bản mới nhất!

### Các nội dung thực hành chi tiết

Vui lòng bấm chọn từng mục dưới đây ở thanh menu bên trái hoặc click trực tiếp vào các liên kết dưới đây để thực hiện chi tiết từng bước:

{{% children /%}}
