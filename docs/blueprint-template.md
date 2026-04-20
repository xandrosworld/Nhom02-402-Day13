# Owner: Pham Le Hoang Nam

# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata

- [GROUP_NAME]: Nhom02-402-Day13
- [REPO_URL]: https://github.com/xandrosworld/Nhom02-402-Day13
- [MEMBERS]:
  - Member A: Mai Tấn Thành | Role: Tech Lead / Integration Owner
  - Member B: Hồ Nhất Khoa | Role: Tracing Owner
  - Member C: Đặng Tùng Anh | Role: PII Owner
  - Member D: Nguyễn Đức Hoàng Phúc | Role: Metrics & Dashboard Owner
  - Member E: Phạm Lê Hoàng Nam | Role: Alerts & Report Owner

---

## 2. Group Performance (Auto-Verified)

- [VALIDATE_LOGS_FINAL_SCORE]: /100
- [TOTAL_TRACES_COUNT]:
- [PII_LEAKS_FOUND]:

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing

- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: docs/evidence/correlation-id.png
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: docs/evidence/pii-redaction.png
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: docs/evidence/trace-waterfall.png
- [TRACE_WATERFALL_EXPLANATION]: (Briefly explain one interesting span in your trace)

### 3.2 Dashboard & SLOs

- [DASHBOARD_6_PANELS_SCREENSHOT]: docs/evidence/dashboard-6-panels.png
- [SLO_TABLE]:
  | SLI | Target | Window | Current Value |
  |---|---:|---|---:|
  | Latency P95 | < 3000ms | 28d | |
  | Error Rate | < 2% | 28d | |
  | Cost Budget | < $2.5/day | 1d | |

### 3.3 Alerts & Runbook

- [ALERT_RULES_SCREENSHOT]: docs/evidence/alert-rules.png
- [SAMPLE_RUNBOOK_LINK]: [docs/alerts.md#1-high-latency-p95](docs/alerts.md#1-high-latency-p95)

---

## 4. Incident Response (Group)

- [SCENARIO_NAME]: (e.g., rag_slow)
- [SYMPTOMS_OBSERVED]:
- [ROOT_CAUSE_PROVED_BY]: (List specific Trace ID or Log Line)
- [FIX_ACTION]:
- [PREVENTIVE_MEASURE]:

---

## 5. Individual Contributions & Evidence

### Mai Tấn Thành

- [TASKS_COMPLETED]:
- [EVIDENCE_LINK]: (Link to specific commit or PR)

### Hồ Nhất Khoa

- [TASKS_COMPLETED]:
- [EVIDENCE_LINK]:

### Đặng Tùng Anh

- [TASKS_COMPLETED]:
- [EVIDENCE_LINK]:

### Nguyễn Đức Hoàng Phúc

- [TASKS_COMPLETED]:
- [EVIDENCE_LINK]:

### Phạm Lê Hoàng Nam

- [TASKS_COMPLETED]: Cấu hình SLO (config/slo.yaml), Alert Rules (config/alert_rules.yaml), viết Runbooks (docs/alerts.md), điền Blueprint report (docs/blueprint-template.md) và Grading evidence (docs/grading-evidence.md)
- [EVIDENCE_LINK]:

---

## 6. Bonus Items (Optional)

- [BONUS_COST_OPTIMIZATION]: (Description + Evidence)
- [BONUS_AUDIT_LOGS]: (Description + Evidence)
- [BONUS_CUSTOM_METRIC]: (Description + Evidence)
