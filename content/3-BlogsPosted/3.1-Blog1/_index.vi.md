---
title: "Blog 1: Rekognition Liveness"
date: 2026-08-10
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# Chống giả mạo nhận diện khuôn mặt với Amazon Rekognition Face Liveness

Khi xây dựng các hệ thống nhận diện khuôn mặt, chúng ta thường gặp phải một lỗ hổng bảo mật kinh điển: **làm sao để ngăn chặn người dùng lấy một bức ảnh chụp sẵn hoặc video quay sẵn trên điện thoại đưa ra trước camera để qua mặt hệ thống?**

Nếu chỉ dùng API `SearchFacesByImage` của Amazon Rekognition, AI sẽ chỉ tìm cách khớp khuôn mặt trong ảnh với database, chứ không biết đó là ảnh chụp người thật hay ảnh chụp lại màn hình điện thoại.

### Giải pháp: Tích hợp Amazon Rekognition Face Liveness

Rất may, AWS đã cung cấp tính năng **Face Liveness** giúp giải quyết triệt để bài toán này. Đây là cách mình đã tích hợp vào hệ thống:

**1. Luồng xử lý:**
- **Bước 1 (Backend):** Khi người dùng quét khuôn mặt, Frontend gọi Backend. Backend gọi API `CreateFaceLivenessSession` của Rekognition để lấy về một `SessionId` duy nhất.
- **Bước 2 (Frontend):** Mình dùng SDK `@aws-amplify/ui-react-liveness`. SDK này hiển thị một giao diện hình bầu dục lên màn hình người dùng, yêu cầu họ đưa mặt vào khung hình. Màn hình sẽ chớp các dải màu ngẫu nhiên (Challenge) để phản chiếu lên khuôn mặt user, trong khi camera stream video trực tiếp về AWS.
- **Bước 3 (Backend):** Sau khi hoàn thành, Frontend báo cho Backend. Backend gọi API `GetFaceLivenessSessionResults` truyền vào `SessionId`.

**2. Đánh giá kết quả (Confidence Score):** 
AWS sẽ trả về một điểm số `Confidence`.
- Nếu **Confidence < 90%**: Khả năng cao là giả mạo (dùng mặt nạ, ảnh 3D, hoặc màn hình iPad). Hệ thống từ chối ngay lập tức.
- Nếu **Confidence >= 90%**: Là người thật. Lúc này, AWS trả kèm hình ảnh khung hình tốt nhất (Reference Image). Mình dùng ảnh này tiếp tục gọi `SearchFacesByImage` để xác định xem đó là nhân viên nào.

### Ưu điểm của kiến trúc này
- **Bảo mật tuyệt đối:** Hoàn toàn loại bỏ được trò gian lận dùng ảnh thẻ hay video quay sẵn.
- **Trải nghiệm mượt mà:** Khác với các hệ thống cũ bắt người dùng phải "chớp mắt 3 lần", "quay đầu sang trái/phải", AWS Liveness chỉ yêu cầu người dùng giữ yên khuôn mặt trong vùng bầu dục, mọi thứ xử lý cực nhanh dưới background.
- **Không lưu trữ video:** Video stream chỉ dùng để phân tích Liveness trong lúc thực thi và tự động bị hủy, đảm bảo tuân thủ quyền riêng tư dữ liệu (Data Privacy).

Hy vọng bài viết này sẽ giúp các bạn giải quyết được bài toán hóc búa khi làm các dự án eKYC hoặc chấm công tự động trên AWS!

### Tài liệu tham khảo
1. [Amazon Rekognition Face Liveness Architecture](https://docs.aws.amazon.com/rekognition/latest/dg/recommendations-liveness.html)
2. [AWS Amplify - Add Face Liveness detection](https://ui.docs.amplify.aws/react/connected-components/liveness)

---
*👉 Link bài viết trên group AWS Study Group: [Cập nhật link sau khi đăng]*