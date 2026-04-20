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

- [VALIDATE_LOGS_FINAL_SCORE]\: /100
- [TOTAL_TRACES_COUNT]\:
- [PII_LEAKS_FOUND]\: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing

- [EVIDENCE_CORRELATION_ID_SCREENSHOT]\: [evidence/correlation-id.png](evidence/correlation-id.png)
- [EVIDENCE_PII_REDACTION_SCREENSHOT]\: [evidence/pii-redaction.png](evidence/pii-redaction.png)
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]\: [evidence/trace-waterfall.png](evidence/trace-waterfall.png)
- [TRACE_WATERFALL_EXPLANATION]\: (Briefly explain one interesting span in your trace)

### 3.2 Dashboard & SLOs

- [DASHBOARD_6_PANELS_SCREENSHOT]\: [evidence/dashboard-6-panels.png](evidence/dashboard-6-panels.png)
- [SLO_TABLE]\:
  | SLI | Target | Window | Current Value |
  |---|---:|---|---:|
  | Latency P95 | < 3000ms | 28d | |
  | Error Rate | < 2% | 28d | |
  | Cost Budget | < $2.5/day | 1d | |

### 3.3 Alerts & Runbook

- [ALERT_RULES_SCREENSHOT]\: [evidence/alert-rules.png](evidence/alert-rules.png)
- [ALERT_DOCS_SCREENSHOT]\: [evidence/alert-docs.png](evidence/alert-docs.png)
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

- [TASKS_COMPLETED]\:
- [EVIDENCE_LINK]\:

### Đặng Tùng Anh

- [TASKS_COMPLETED]\: Đã ẩn và mã hóa thành công email, thẻ tín dụng (`[REDACTED_CREDIT_CARD]`), CCCD (`[REDACTED_CCCD]`), Số điện thoại khu vực VN (`[REDACTED_PHONE_VN]`), cũng như add thêm cụm từ khóa bắt Hộ chiếu (Passport) và Địa chỉ nhà.
- [EVIDENCE_LINK]\: [evidence/pii-redaction.png](evidence/pii-redaction.png)

### Nguyễn Đức Hoàng Phúc

- [TASKS_COMPLETED]\:
- [EVIDENCE_LINK]\:

### Phạm Lê Hoàng Nam

- [TASKS_COMPLETED]\: Cấu hình 6 cảnh báo mức P1-P3 trong `config/alert_rules.yaml`, biên soạn runbook xử lý sự cố trong `docs/alerts.md`, thiết lập thông số cho `config/slo.yaml`, và tổng hợp hoàn thiện báo cáo Lab (Blueprint + Grading Evidence).
- [EVIDENCE_LINK]\: [evidence/alert-rules.png](evidence/alert-rules.png)
- [RUNBOOK_EVIDENCE]\: [evidence/alert-doc.png](evidence/alert-doc.png)

---

## 6. Bonus Items (Optional)

- [BONUS_COST_OPTIMIZATION]\: (Description + Evidence)
- [BONUS_AUDIT_LOGS]\: (Description + Evidence)
- [BONUS_CUSTOM_METRIC]\: (Description + Evidence)
