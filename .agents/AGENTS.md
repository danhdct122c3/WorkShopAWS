# Workshop Content Generation Rules

The following rules apply when generating or editing the workshop content in this repository:

1. **Tuân thủ tuyệt đối hình ảnh thực tế (Truth in Screenshots)**
   Mọi nội dung hướng dẫn (từ API Gateway, WAF, DynamoDB đến S3) đều được viết lại bám sát 100% vào các ảnh chụp màn hình được lưu trong `static/aws-image/`, tuyệt đối không đoán mò cấu hình.

2. **Đối chiếu chéo với Backend Code**
   Luôn kiểm tra đối chiếu (cross-reference) với mã nguồn thực tế (như file `.env` trong thư mục backend của dự án gốc) để đảm bảo mô tả kiến trúc hệ thống chính xác (điển hình như việc phát hiện ra 9 bảng DynamoDB thay vì 3 bảng).

3. **Mô tả toàn diện nhưng Thực hành tối giản (Demo Notes)**
   Trong tài liệu, luôn mô tả hệ thống ở mức độ hoàn chỉnh nhất (ví dụ: cần 9 bảng), nhưng luôn kèm theo một thẻ `[LƯU Ý QUAN TRỌNG CHO BÀI DEMO]` (dùng markdown quote `>`) để cho phép học viên làm tắt (ví dụ: chỉ tạo 1 bảng) nhằm tiết kiệm thời gian mà vẫn hiểu nguyên lý.

4. **Trình bày cấu trúc thông minh, tránh lặp lại**
   Sử dụng Markdown Table để tổng hợp các cấu hình có tính chất lặp lại (như danh sách các bảng, các khóa PK/GSI). Phần thao tác từng bước (Step-by-step) chỉ hướng dẫn chi tiết cho 1 tài nguyên đại diện, sau đó yêu cầu học viên tự lặp lại cho các tài nguyên khác trong bảng để tránh văn bản lặp lại nhàm chán.
