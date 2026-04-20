# Phân Công Nhóm Day 13

## Thành viên

| Thành viên | Vai trò | Phạm vi chính |
|---|---|---|
| Mai Tấn Thành | Tech Lead / Integration Owner | Logging pipeline, correlation ID, tích hợp hệ thống, merge cuối |
| Hồ Nhất Khoa | Tracing Owner | Setup Langfuse, kiểm tra trace, chụp evidence trace |
| Đặng Tùng Anh | PII Owner | Pattern scrub PII, test, kiểm tra rò rỉ log |
| Nguyễn Đức Hoàng Phúc | Metrics & Dashboard Owner | Metrics, load test, dashboard, evidence incident |
| Phạm Lê Hoàng Nam | Alerts & Report Owner | SLO, alert rules, runbook, blueprint report |

## Quy ước làm việc

1. Mai Tấn Thành chuẩn bị repo starter và merge tích hợp cuối.
2. Mỗi người tạo branch riêng từ `main`.
3. Mỗi người chỉ sửa phần file mình phụ trách, tránh đụng file của người khác nếu không cần.
4. Nếu cần sửa chéo file, phải báo owner file đó trước khi merge.
5. Mỗi người phải giữ ít nhất một commit rõ ràng để làm bằng chứng cá nhân.

## Phân file theo người

### Mai Tấn Thành
- `app/middleware.py`
- `app/main.py`
- `app/logging_config.py`
- kiểm tra tích hợp cuối bằng `scripts/validate_logs.py`

### Hồ Nhất Khoa
- `app/tracing.py`
- kiểm tra trace trong `app/agent.py`
- setup Langfuse trong `.env` trên máy local
- chụp evidence từ giao diện Langfuse

### Đặng Tùng Anh
- `app/pii.py`
- `tests/test_pii.py`
- kiểm tra rò rỉ log bằng `data/sample_queries.jsonl`

### Nguyễn Đức Hoàng Phúc
- `app/metrics.py`
- `scripts/load_test.py`
- dựng dashboard từ `/metrics`
- test incident bằng `scripts/inject_incident.py`

### Phạm Lê Hoàng Nam
- `config/slo.yaml`
- `config/alert_rules.yaml`
- `docs/alerts.md`
- `docs/blueprint-template.md`
- `docs/grading-evidence.md`

## Kết quả mỗi người cần bàn giao

### Mai Tấn Thành
- correlation ID chạy xuyên suốt request
- log API có đủ `user_id_hash`, `session_id`, `feature`, `model`, `env`
- response headers có `x-request-id` và `x-response-time-ms`

### Hồ Nhất Khoa
- có ít nhất 10 traces trên Langfuse
- có 1 ảnh trace waterfall
- trace có metadata user/session/tags

### Đặng Tùng Anh
- log không lộ email, số điện thoại, CCCD, thẻ tín dụng
- test cho các pattern PII chính chạy pass
- giải thích được ví dụ trước/sau khi scrub

### Nguyễn Đức Hoàng Phúc
- dashboard có đủ 6 panel theo yêu cầu
- load test tạo đủ dữ liệu cho biểu đồ
- demo được incident qua metrics

### Phạm Lê Hoàng Nam
- alert rules trỏ đúng runbook
- bảng SLO được điền đủ giá trị cuối
- blueprint report hoàn chỉnh

## Gợi ý tên branch

- `mtt/logging-integration`
- `khoa/tracing`
- `anh/pii`
- `phuc/metrics-dashboard`
- `nam/alerts-report`

## Quy trình làm starter

1. Repo starter đã được push lên repo nhóm.
2. Mọi người clone repo và tạo branch riêng ngay.
3. Mai Tấn Thành giữ phần tích hợp và kiểm tra cuối.
4. Các thành viên còn lại làm song song theo đúng file phụ trách.
5. Thứ tự merge khuyến nghị: PII -> tracing -> metrics/dashboard -> alerts/report -> integration cuối.
