---
title : "Data Lake & Worker"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 5.7.1. </b> "
---

#### Khởi tạo Data Lake và Analytics Worker
Trước khi dùng Glue và Athena để phân tích dữ liệu, ta cần một nơi lưu trữ dữ liệu (S3 Data Lake) và một đoạn mã để tự động đẩy sự kiện điểm danh từ SQS vào Data Lake này. Kiến trúc ghi trực tiếp từ Lambda vào S3 rất phổ biến cho các luồng dữ liệu vừa và nhỏ, giúp tiết kiệm chi phí so với việc dùng Kinesis Firehose.

**Bước 1: Tạo S3 Data Lake Bucket**
Đầu tiên, ta cần một chỗ chứa các file log điểm danh.
1. Tìm kiếm và truy cập dịch vụ **S3** trên AWS Console, bấm **Create bucket**.
> ![Tìm kiếm S3](/aws-image/setupS3/setups3-1.png)
> ![Bấm Create bucket](/aws-image/setupS3/s3-2.png)
2. **Bucket name**: Đặt tên là `smart-campus-datalake-[tên-bạn]` (Ví dụ: `smart-campus-datalake-danhdct`).
> ![Nhập tên bucket](/aws-image/setupS3Worker/s31.png)
3. Giữ nguyên toàn bộ các cài đặt mặc định (để bucket này ở chế độ Private, chặn toàn bộ Public Access là an toàn nhất).
> ![Object Ownership](/aws-image/setupS3Worker/s32.png)
> ![Block Public Access](/aws-image/setupS3Worker/s33.png)
4. Cuộn xuống cuối bấm **Create bucket**.
> ![Tạo S3 Data Lake](/aws-image/setupS3Worker/s34.png)
5. Màn hình báo tạo Bucket thành công.
> ![Tạo thành công](/aws-image/setupS3Worker/s35.png)

**Bước 2: Tạo hàm Lambda Analytics Worker**
Bây giờ ta cần tạo một hàm Lambda đóng vai trò "công nhân": Đọc sự kiện từ hàng đợi SQS và ghi file JSON trực tiếp lên S3 Data Lake.
1. Vào dịch vụ **Lambda** -> **Create function**.
> ![Tìm kiếm Lambda](/aws-image/setupLambda/lambda3.png)
> ![Vào Create function](/aws-image/setupLambda/lambda4.png)
2. **Function name**: `smart-campus-analytics-worker`. Chọn Runtime là **Python 3.11** (hoặc 3.x).
3. Bấm **Create function**.
> ![Điền thông tin và Tạo hàm](/aws-image/setupLambdaWorker/lambda1.png)
> ![Tạo thành công](/aws-image/setupLambdaWorker/lambda2.png)
4. Trong màn hình Lambda, cuộn xuống tab **Code**: Mở file `analytics_worker.py` trong source code thư mục `backend/app/workers/`, copy toàn bộ nội dung (hoặc copy đoạn code dưới đây) dán đè vào file `lambda_function.py` trên giao diện.
```python
"""Analytics Worker (Workflow 5 – Analytics Pipeline).

Consumes AttendanceRecorded events from EventBridge and streams data to:
    S3 Data Lake (Direct Put) → Glue Catalog → Athena → QuickSight

Published Events:
    None (fire-and-forget streaming)
"""

import json
import logging
import boto3
import uuid
from functools import lru_cache

from app.core.config import settings
from app.shared.aws.eventbridge import publish_event

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@lru_cache
def get_s3_client():
    return boto3.client("s3", region_name=settings.aws_region)


def _write_to_s3(record: dict) -> str:
    """Stream a single attendance record directly to S3 Data Lake."""
    client = get_s3_client()
    data = json.dumps(record, ensure_ascii=False, default=str)
    
    # Generate unique filename with partitioning prefix
    year = record.get("year", "0000")
    month = record.get("month", "00")
    day = record.get("day", "00")
    file_name = f"year={year}/month={month}/day={day}/{uuid.uuid4().hex}.json"
    
    client.put_object(
        Bucket=settings.data_lake_bucket,
        Key=file_name,
        Body=data.encode("utf-8"),
        ContentType="application/json"
    )
    return file_name


def handler(event: dict, context) -> dict:
    """
    AWS Lambda entry point for Analytics Worker.

    Triggered by SQS Queue (smart-campus-analytics-queue) containing batches
    of EventBridge 'AttendanceRecorded' events.
    """
    records = event.get("Records", [])
    logger.info("AnalyticsWorker (SQS) received %d records", len(records))

    failed_message_ids = []

    for record in records:
        message_id = record.get("messageId")
        try:
            # EventBridge payload is embedded in the SQS body
            body_str = record.get("body", "{}")
            eb_event = json.loads(body_str)
            
            detail_type = eb_event.get("detail-type", "")
            detail = eb_event.get("detail", {})

            if detail_type != "AttendanceRecorded":
                logger.info("Skipping non-attendance event: %s (MsgId: %s)", detail_type, message_id)
                continue

            # Build analytics record (flattened for Athena/QuickSight)
            analytics_record = {
                "event_type": detail_type,
                "attendance_id": detail.get("attendanceId"),
                "user_id": detail.get("userId"),
                "status": detail.get("status"),
                "timestamp": detail.get("timestamp"),
                # Partitioning fields for Glue/Athena
                "year": detail.get("timestamp", "")[:4] if detail.get("timestamp") else None,
                "month": detail.get("timestamp", "")[5:7] if detail.get("timestamp") else None,
                "day": detail.get("timestamp", "")[8:10] if detail.get("timestamp") else None,
            }

            record_id = _write_to_s3(analytics_record)
            logger.info("Wrote to S3 Data Lake. MsgId=%s, File=%s", message_id, record_id)

        except Exception as exc:
            logger.error("Failed to process message %s: %s", message_id, exc, exc_info=True)
            failed_message_ids.append(message_id)

    # Return partial batch failure standard format
    return {
        "batchItemFailures": [{"itemIdentifier": msg_id} for msg_id in failed_message_ids]
    }
```
> ![Dán Code](/aws-image/setupLambdaWorker/lambda3.png)
5. Cấu hình biến môi trường: Chuyển sang tab **Configuration** -> **Environment variables**. Bấm **Edit**, thêm biến `DATA_LAKE_BUCKET` với giá trị là tên bucket bạn vừa tạo. Bấm **Save**. 
> ![Tab Configuration](/aws-image/setupLambdaWorker/lambda4.png)
> ![Nhập Key Value](/aws-image/setupLambdaWorker/lambda5.png)
6. Trở lại tab **Code**, bấm **Deploy** (Trên màn hình sẽ hiện dòng thông báo xanh lá cây khi cập nhật thành công).
> ![Deploy thành công](/aws-image/setupLambdaWorker/lambda6.png)

**Bước 3: Cấu hình Trigger và Phân quyền**
1. Cấu hình **Trigger** (Kích hoạt):
   - Ở biểu đồ trên cùng (Function overview), bấm **+ Add trigger**.
   - Trình đơn thả xuống chọn **SQS**.
   - SQS queue: Chọn hàng đợi `smart-campus-analytics-queue` bạn đã tạo ở bài 5.6.3. Bấm **Add**.
> ![Thêm SQS Trigger](/aws-image/setupSQS/sqs24.png)
2. Cấp quyền **IAM** (Cực kỳ quan trọng):
   - Chuyển sang tab **Configuration** -> **Permissions** -> Bấm vào tên Role (VD: `smart-campus-analytics-worker-role...`) để mở cửa sổ IAM.
> ![Mở IAM Role](/aws-image/setupLambdaWorker/lambda7.png)
   - Trong IAM, bấm **Add permissions** -> **Attach policies**.
> ![Attach policies](/aws-image/setupLambdaWorker/lambda8.png)
   - Tìm và thêm 2 quyền: `AmazonS3FullAccess` và `AmazonSQSFullAccess`. Bấm **Add permissions**.
> ![Thêm S3 Access](/aws-image/setupLambdaWorker/lambda9.png)
> ![Thêm SQS Access](/aws-image/setupLambdaWorker/lambda10.png)

**Bước 4: Test luồng dữ liệu**
1. Gọi thử API điểm danh bằng Postman (hoặc Frontend) để giả lập sinh viên quét khuôn mặt.
2. Đợi vài giây, mở S3 Bucket `smart-campus-datalake-[tên-bạn]`.
3. Mở S3 Console, vào Bucket Data Lake vừa tạo. Bạn sẽ thấy một cấu trúc thư mục tự động được sinh ra: `attendance/year=.../month=.../day=.../`. Bên trong là các file dữ liệu dạng JSON. Xin chúc mừng, Data Lake của bạn đã chính thức đi vào hoạt động!
> ![Kết quả S3 1](/aws-image/setupLambdaWorker/lambda11.png)
> ![Kết quả S3 2](/aws-image/setupLambdaWorker/lambda12.png)
> ![Kết quả S3 3](/aws-image/setupLambdaWorker/lambda13.png)
> ![Kết quả S3 4](/aws-image/setupLambdaWorker/lambda14.png)
> ![Kết quả S3 5](/aws-image/setupLambdaWorker/lambda15.png)

Tuyệt vời! Bây giờ luồng dữ liệu từ lúc điểm danh đến lúc ghi vào Data Lake đã hoàn toàn tự động. Sang bài tiếp theo, chúng ta sẽ cho AWS Glue vào cuộc để quét các file JSON này.
