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
5. Mỗi người nên có ít nhất một commit rõ ràng cho phần việc của mình.
6. Ảnh evidence phải đẩy lên thư mục `docs/evidence/` đúng tên file đã quy ước.

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
- có trace waterfall để giải thích trong demo
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

## Evidence cần nộp của từng người

### Mai Tấn Thành
- up ảnh log có `correlation_id` vào `docs/evidence/correlation-id.png`
- nếu có thêm ảnh log validate hoặc flow request thì có thể up thêm vào `docs/evidence/`

### Hồ Nhất Khoa
- up ảnh danh sách trace vào `docs/evidence/trace-list.png`
- up ảnh trace waterfall vào `docs/evidence/trace-waterfall.png`
- gửi cho Nam số lượng traces cuối cùng và giải thích ngắn 1 trace nếu cần

### Đặng Tùng Anh
- up ảnh log đã redact PII vào `docs/evidence/pii-redaction.png`
- nếu có ảnh test pass thì có thể up thêm vào `docs/evidence/`
- gửi cho Nam mô tả ngắn những pattern PII đã thêm

### Nguyễn Đức Hoàng Phúc
- up ảnh dashboard vào `docs/evidence/dashboard-6-panels.png`
- nếu có ảnh incident trước/sau khi inject thì up vào `docs/evidence/incident-before-after.png`
- gửi cho Nam số liệu chính để điền bảng SLO nếu cần

### Phạm Lê Hoàng Nam
- up ảnh alert rules vào `docs/evidence/alert-rules.png`
- kéo toàn bộ ảnh evidence từ repo về rồi điền `docs/blueprint-template.md`
- dùng `docs/grading-evidence.md` làm checklist xem đã đủ evidence chưa

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
5. Sau khi làm xong, mỗi người nhớ đẩy ảnh evidence của mình vào `docs/evidence/`.
6. Nam kéo code và ảnh mới nhất về, rồi hoàn thiện report cuối.
