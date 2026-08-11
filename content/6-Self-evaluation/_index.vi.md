---
title: "Tự đánh giá"
date: 2026-08-09
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

Trong suốt thời gian thực tập tại **FCAJ (First Cloud AI Journey)** từ ngày **22/06/2026** đến **15/08/2026**, mình đã có cơ hội học hỏi, rèn luyện và áp dụng kiến thức lập trình vào môi trường thực tế trên nền tảng điện toán đám mây AWS.

Trong dự án **Smart Campus Platform**, mình đảm nhiệm vai trò chính là **Backend Developer**. Nhiệm vụ cốt lõi của mình là thiết kế cơ sở dữ liệu NoSQL, phát triển các API bằng framework **FastAPI**, và đặc biệt là đưa ra các **giải pháp kỹ thuật (Solutions)** để xử lý các bài toán nghiệp vụ phức tạp. Cụ thể, mình đã trực tiếp đề xuất và thiết kế các luồng xử lý như: 
- Giải quyết bài toán tải file báo cáo dung lượng lớn tránh quá tải API Gateway bằng giải pháp **Amazon S3 Presigned URL**.
- Tối ưu hóa truy vấn dữ liệu điểm danh và công việc bằng kỹ thuật **Denormalization** và tạo Global Secondary Index (GSI) trên **Amazon DynamoDB**.
- Bảo mật hệ thống với kiến trúc xác thực đa lớp, tích hợp **Amazon Cognito** kết hợp viết Middleware chặn và giải mã JWT Token (python-jose).
- Thiết kế hệ thống phân quyền linh hoạt (Role-Based Access Control) cho Admin, Manager và Staff.
- Đóng gói toàn bộ Backend thành kiến trúc Serverless siêu tốc với thư viện **Mangum** chạy trên **AWS Lambda** & **Amazon API Gateway**.

Về tác phong làm việc, mình luôn cố gắng hoàn thành nhiệm vụ đúng hạn, chủ động tìm hiểu tài liệu kỹ thuật để đưa ra các kiến trúc tối ưu nhất (Best Practices), đồng thời tích cực hỗ trợ các thành viên khác trong nhóm (Frontend, DevOps) để quá trình tích hợp hệ thống diễn ra mượt mà nhất.

Để phản ánh một cách khách quan quá trình thực tập, mình xin tự đánh giá bản thân theo các tiêu chí dưới đây:

| STT | Tiêu chí | Mô tả | Tốt | Khá | Trung bình |
|-----|----------|-------|:---:|:---:|:----------:|
| 1 | **Kiến thức chuyên môn** | Nắm vững kiến trúc Serverless AWS và phát triển API với FastAPI. | ✅ | ☐ | ☐ |
| 2 | **Khả năng học hỏi** | Tiếp thu nhanh công nghệ mới và tự giải quyết các vấn đề kỹ thuật. | ✅ | ☐ | ☐ |
| 3 | **Sự chủ động** | Tự giác tìm hiểu tài liệu và đề xuất các giải pháp kiến trúc phù hợp. | ✅ | ☐ | ☐ |
| 4 | **Trách nhiệm** | Đảm bảo hoàn thành đúng tiến độ các nhiệm vụ Backend được giao. | ✅ | ☐ | ☐ |
| 5 | **Kỷ luật** | Tuân thủ nội quy, lịch họp và cập nhật tiến độ công việc đầy đủ. | ☐ | ✅ | ☐ |
| 6 | **Cầu tiến** | Không ngừng tối ưu code và cập nhật các best practice từ AWS. | ✅ | ☐ | ☐ |
| 7 | **Giao tiếp** | Trao đổi thông tin rõ ràng, hiệu quả với các thành viên trong nhóm. | ☐ | ✅ | ☐ |
| 8 | **Hợp tác nhóm** | Phối hợp tốt với team Frontend và DevOps để tích hợp hệ thống. | ✅ | ☐ | ☐ |
| 9 | **Ứng xử** | Luôn lắng nghe góp ý, giữ thái độ hòa nhã và chuyên nghiệp. | ✅ | ☐ | ☐ |
| 10 | **Giải quyết vấn đề** | Phân tích bài toán logic tốt, biết cách xử lý lỗi hệ thống hiệu quả. | ☐ | ✅ | ☐ |
| 11 | **Đóng góp** | Xây dựng thành công toàn bộ hệ thống Backend cho Smart Campus. | ✅ | ☐ | ☐ |
| 12 | **Đánh giá chung** | Hoàn thành tốt mục tiêu thực tập, tích lũy nhiều kinh nghiệm thực tế. | ✅ | ☐ | ☐ |

### Cần cải thiện

* **Kỷ luật ước lượng thời gian:** Cần luyện kỹ năng phân tách task nhỏ hơn và đặt time-box rõ ràng, tránh để một bug phức tạp tiêu tốn quá nhiều thời gian mà không có checkpoint để đánh giá lại hướng tiếp cận.
* **Đọc hiểu tài liệu kỹ thuật tiếng Anh:** Cần nâng cao tốc độ đọc AWS documentation gốc tiếng Anh, giảm sự phụ thuộc vào các tutorial trên mạng để tiếp cận thông tin chính xác hơn.
* **Kỹ năng trình bày:** Cần luyện thêm khả năng giải trình bày, giải thích vấn đề.
* **Tư duy debug có hệ thống:** Khi gặp lỗi, cần có thói quen check Amazon CloudWatch Logs kỹ càng và kiểm tra từng lớp thay vì tìm vùng lỗi theo cảm tính.