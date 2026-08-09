---
title : "Tăng tốc với CloudFront"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 5.8.2. </b> "
---

#### Khởi tạo Amazon CloudFront (CDN)
Mặc dù S3 có thể dùng để host website, nhưng nó không hỗ trợ chứng chỉ SSL (HTTPS) cho tên miền tuỳ chỉnh và cũng không có bộ đệm (cache) toàn cầu. Amazon CloudFront giải quyết toàn bộ các vấn đề này.

**Bước 1: Tạo CloudFront Distribution**

1. Từ Console, tìm kiếm dịch vụ **CloudFront** và bấm **Create distribution**.
2. **Origin domain**: Bấm vào ô này và chọn S3 Bucket bạn vừa tạo (Ví dụ: `smart-campus-frontend-2024.s3.amazonaws.com`).
> ![Chọn S3 Origin](/aws-image/setupCloudfront/cloudfront1.png)
3. **Origin access**: Thay vì chọn Public, hãy chọn **Origin access control settings (recommended)**.
> ![Cấu hình OAC 1](/aws-image/setupCloudfront/cloudfront2.png)
4. Bấm **Create control setting** > Dùng các thiết lập mặc định và bấm **Create**.
> ![Cấu hình OAC 2](/aws-image/setupCloudfront/cloudfront3.png)
5. CloudFront sẽ thông báo bạn cần cập nhật S3 bucket policy. Bạn sẽ thấy dòng "You must update the S3 bucket policy".
> ![Thông báo S3 Policy](/aws-image/setupCloudfront/cloudfront4.png)
6. **Default cache behavior**: Ở mục **Viewer protocol policy**, chọn **Redirect HTTP to HTTPS** để ép buộc dùng kết nối an toàn. Ở phần **Cache key and origin requests**, chọn **Cache policy and origin request policy** và chọn policy `CachingOptimized`.
> ![Cấu hình Cache](/aws-image/setupCloudfront/cloudfront5.png)
7. Cuộn xuống phần **Web Application Firewall (WAF)**: Bạn có thể chọn *Do not enable security protections*. Ở mục **Default root object**, nhập `index.html`. Bấm **Create distribution**.
> ![WAF và Create](/aws-image/setupCloudfront/cloudfront6.png)

**Bước 2: Cập nhật S3 Bucket Policy**

1. Ngay sau khi tạo Distribution thành công, bạn sẽ thấy thông báo màu xanh lam nhạt gợi ý sao chép Bucket Policy. Bấm nút **Copy policy**.
> ![Copy Policy](/aws-image/setupCloudfront/cloudfront7.png)
2. Mở S3 Bucket của bạn, vào tab Permissions, Edit Bucket policy và dán đoạn mã JSON vừa copy (đoạn này cho phép CloudFront đọc file). Bấm Save.
> ![Dán Policy](/aws-image/setupCloudfront/cloudfront8.png)

**Bước 3: Truy cập trang web qua CDN**

1. Quay lại trang chi tiết của CloudFront, ở phần General, sao chép địa chỉ **Distribution domain name** (Ví dụ: `d...cloudfront.net`).
> ![Domain CloudFront](/aws-image/setupCloudfront/cloudfront9.png)
2. Mở trình duyệt và dán đường link vào. Bạn sẽ thấy trang web load cực nhanh với ổ khóa HTTPS an toàn!
