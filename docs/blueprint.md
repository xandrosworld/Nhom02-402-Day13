# Owner: Pham Le Hoang Nam

# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata

- [GROUP_NAME]\: Nhom02-402-Day13
- [REPO_URL]\: https://github.com/xandrosworld/Nhom02-402-Day13
- [MEMBERS]\:
  - Member A: Mai Tấn Thành | Role: Tech Lead / Integration Owner
  - Member B: Hồ Nhất Khoa | Role: Tracing Owner
  - Member C: Đặng Tùng Anh | Role: PII Owner
  - Member D: Nguyễn Đức Hoàng Phúc | Role: Metrics & Dashboard Owner
  - Member E: Phạm Lê Hoàng Nam | Role: Alerts & Report Owner

---

## 2. Group Performance (Auto-Verified)

- [VALIDATE_LOGS_FINAL_SCORE]\: 100/100
- [TOTAL_TRACES_COUNT]\: 58
- [PII_LEAKS_FOUND]\: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing

- [EVIDENCE_CORRELATION_ID_SCREENSHOT]\: [evidence/correlation-id.png](evidence/correlation-id.png)
- [EVIDENCE_PII_REDACTION_SCREENSHOT]\: [evidence/pii-redaction.png](evidence/pii-redaction.png)
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]\: [evidence/trace-waterfall.png](evidence/trace-waterfall.png)
- [TRACE_WATERFALL_EXPLANATION]\: Trace “How should alerts be designed?” cho thấy span end-to-end của pipeline RAG với latency khoảng 0.54s, tokens_in 29, tokens_out 149, cost_usd ~0.0023. Metadata gắn model và tags theo session, giúp debug nhanh theo feature/model.

### 3.2 Dashboard & SLOs

- [DASHBOARD_6_PANELS_SCREENSHOT]\: [evidence/dashboard-6-panels.png](evidence/dashboard-6-panels.png)
- [SLO_TABLE]\:
  | SLI | Target | Window | Current Value |
  |---|---:|---|---:|
  | Latency P95 | < 3000ms | 28d | 155ms |
  | Error Rate | < 2% | 28d | pending |
  | Cost Budget | < $2.5/day | 1d | $0.0183 (sample run) |

### 3.3 Alerts & Runbook

- [ALERT_RULES_SCREENSHOT]\: [evidence/alert-rules.png](evidence/alert-rules.png)
- [ALERT_DOCS_SCREENSHOT]\: [evidence/alert-doc.png](evidence/alert-doc.png)
- [RUNBOOK_LINK]\: [alerts.md](alerts.md)

---

## 4. Incident Response (Group)

- [SCENARIO_NAME]\: (e.g., rag_slow)
- [SYMPTOMS_OBSERVED]\:
- [ROOT_CAUSE_PROVED_BY]\: (List specific Trace ID or Log Line)
- [FIX_ACTION]\:
- [PREVENTIVE_MEASURE]\:

---

## 5. Individual Contributions & Evidence

### Mai Tấn Thành

- [TASKS_COMPLETED]\: Tích hợp middleware xử lý sinh và truyền `correlation_id` (vd: `req-da313bf8`). Bind đầy đủ các tag ngữ cảnh (`user_id_hash`, `session_id`, `feature`, `model`, `env`) vào cấu trúc log.
- [EVIDENCE_LINK]\: [evidence/correlation-id.png](evidence/correlation-id.png)

### Hồ Nhất Khoa

- [TASKS_COMPLETED]\: Triển khai toàn bộ Langfuse tracing integration trong `app/tracing.py`. Cụ thể: (1) lazy initialization với `get_client()` và graceful fallback no-ops khi thiếu credentials, đảm bảo app chạy được cả khi không có Langfuse; (2) export `observe()` decorator được áp dụng trực tiếp lên `LabAgent.run()` trong `app/agent.py`, tạo trace span bao toàn bộ pipeline RAG; (3) `update_current_trace()` gắn `user_id` đã hash SHA256, `session_id`, và tags `["lab", feature, model]` vào mỗi trace; (4) `update_current_observation()` gắn metadata `doc_count`, `query_preview` (đã scrub PII), `input`, `output` vào span; (5) `tracing_enabled()` được dùng bởi `/health` endpoint để báo cáo trạng thái Langfuse; (6) setup `LANGFUSE_BASE_URL` tự động từ `LANGFUSE_HOST` để tương thích cả self-hosted lẫn cloud.
- [EVIDENCE_LINK]\: [evidence/trace-list.png](evidence/trace-list.png) | [evidence/trace-waterfall.png](evidence/trace-waterfall.png)

### Đặng Tùng Anh

- [TASKS_COMPLETED]\: Đã ẩn và mã hóa thành công email, thẻ tín dụng ([REDACTED_CREDIT_CARD]), CCCD ([REDACTED_CCCD]), Số điện thoại khu vực VN ([REDACTED_PHONE_VN]), cũng như add thêm cụm từ khóa bắt Hộ chiếu (Passport) và Địa chỉ nhà. Hoàn thiện bộ Unit Test với Pytest cho mọi định dạng PII trên, đảm bảo filter hoạt động chính xác tuyệt đối.

- [EVIDENCE_LINK]\: [evidence/pii-redaction.png](evidence/pii-redaction.png)

### Nguyễn Đức Hoàng Phúc

- [TASKS_COMPLETED]\: Xây dựng module metrics trong `app/metrics.py` để tổng hợp các chỉ số chính của hệ thống gồm traffic, latency P50/P95/P99, error breakdown, cost, token usage và quality score. Hoàn thiện script `scripts/load_test.py` để tạo tải và sinh dữ liệu thực tế cho dashboard. Sử dụng endpoint `/metrics` làm nguồn dựng dashboard theo đúng `docs/dashboard-spec.md` với đủ 6 panel bắt buộc: latency, traffic, error rate, cost, tokens và quality proxy. Đồng thời hỗ trợ demo incident bằng `scripts/inject_incident.py` với các kịch bản `rag_slow`, `tool_fail`, `cost_spike` để quan sát sự thay đổi của metrics trước và sau khi inject lỗi.
- [EVIDENCE_LINK]\: [evidence/dashboard-6-panels.png](evidence/dashboard-6-panels.png)
- [EVIDENCE_LINK]\: [evidence/before.png](evidence/before.png)
- [EVIDENCE_LINK]\: [evidence/after.png](evidence/after.png)

### Phạm Lê Hoàng Nam

- [TASKS_COMPLETED]\: Cấu hình 6 cảnh báo mức P1-P3 trong `config/alert_rules.yaml`, biên soạn runbook xử lý sự cố trong `docs/alerts.md`, thiết lập thông số cho `config/slo.yaml`, và tổng hợp hoàn thiện báo cáo Lab (Blueprint + Grading Evidence).
- [EVIDENCE_LINK]\: [evidence/alert-rules.png](evidence/alert-rules.png)
- [RUNBOOK_EVIDENCE]\: [evidence/alert-doc.png](evidence/alert-doc.png)

---

## 6. Bonus Items (Optional)

- [BONUS_COST_OPTIMIZATION]\: (Description + Evidence)
- [BONUS_AUDIT_LOGS]\: (Description + Evidence)
- [BONUS_CUSTOM_METRIC]\: (Description + Evidence)
