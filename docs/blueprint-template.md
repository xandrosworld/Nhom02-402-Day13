# Owner: Pham Le Hoang Nam

# Day 13 Observability Lab Report

> This file mirrors `docs/blueprint.md` so older repo references still work.

## 1. Team Metadata

- [GROUP_NAME]: Nhom02-402-Day13
- [REPO_URL]: https://github.com/xandrosworld/Nhom02-402-Day13
- [MEMBERS]:
  - Member A: Mai Tan Thanh | Role: Tech Lead / Integration Owner
  - Member B: Ho Nhat Khoa | Role: Tracing Owner
  - Member C: Dang Tung Anh | Role: PII Owner
  - Member D: Nguyen Duc Hoang Phuc | Role: Metrics & Dashboard Owner
  - Member E: Pham Le Hoang Nam | Role: Alerts & Report Owner

---

## 2. Group Performance (Auto-Verified)

- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: 58
- [PII_LEAKS_FOUND]: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing

- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: [evidence/correlation-id.png](evidence/correlation-id.png)
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: [evidence/pii-redaction.png](evidence/pii-redaction.png)
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: [evidence/trace-waterfall.png](evidence/trace-waterfall.png)
- [TRACE_WATERFALL_EXPLANATION]: The trace for "How should alerts be designed?" shows the full RAG flow end-to-end. The trace records request metadata, model tags, token usage, and total latency around 0.54s, which makes it easy to debug by feature and model.

### 3.2 Dashboard & SLOs

- [DASHBOARD_6_PANELS_SCREENSHOT]: [evidence/dashboard-6-panels.png](evidence/dashboard-6-panels.png)
- [SLO_TABLE]:
| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | 155ms |
| Error Rate | < 2% | 28d | 0% |
| Cost Budget | < $2.5/day | 1d | $0.0183 (sample run) |

### 3.3 Alerts & Runbook

- [ALERT_RULES_SCREENSHOT]: [evidence/alert-rules.png](evidence/alert-rules.png)
- [ALERT_DOCS_SCREENSHOT]: [evidence/alert-doc.png](evidence/alert-doc.png)
- [RUNBOOK_LINK]: [alerts.md](alerts.md)

---

## 4. Incident Response (Group)

- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: Dashboard latency increased after enabling the incident. The before/after screenshots show higher tail latency, while traces became noticeably slower for the same request patterns.
- [ROOT_CAUSE_PROVED_BY]: The trace waterfall and before/after dashboard screenshots point to retrieval slowdown. The code path in `app/mock_rag.py` confirms that enabling `rag_slow` adds a `time.sleep(2.5)` delay in retrieval.
- [FIX_ACTION]: Disable the `rag_slow` toggle and rerun requests to confirm latency recovers to baseline.
- [PREVENTIVE_MEASURE]: Keep the latency alert active, monitor P95 from the dashboard, and use the runbook to inspect traces before wider user impact.

---

## 5. Individual Contributions & Evidence

### Mai Tan Thanh

- [TASKS_COMPLETED]: Integrated middleware to generate and propagate `correlation_id`, and bound `user_id_hash`, `session_id`, `feature`, `model`, and `env` into structured API logs.
- [EVIDENCE_LINK]: [evidence/correlation-id.png](evidence/correlation-id.png)

### Ho Nhat Khoa

- [TASKS_COMPLETED]: Implemented Langfuse tracing in `app/tracing.py`, wired the `observe()` decorator into `LabAgent.run()`, added trace/session tags, and ensured traces can be verified from the `/health` and Langfuse UI.
- [EVIDENCE_LINK]: [evidence/trace-list.png](evidence/trace-list.png) | [evidence/trace-waterfall.png](evidence/trace-waterfall.png)

### Dang Tung Anh

- [TASKS_COMPLETED]: Added PII protection for email, phone, CCCD, credit card, passport, and Vietnamese-style address patterns, and completed the related pytest coverage.
- [EVIDENCE_LINK]: [evidence/pii-redaction.png](evidence/pii-redaction.png)

### Nguyen Duc Hoang Phuc

- [TASKS_COMPLETED]: Built the metrics aggregation path, produced dashboard evidence from `/metrics`, and supported the incident demonstration with before/after dashboard screenshots.
- [EVIDENCE_LINK]: [evidence/dashboard-6-panels.png](evidence/dashboard-6-panels.png) | [evidence/before.png](evidence/before.png) | [evidence/after.png](evidence/after.png)

### Pham Le Hoang Nam

- [TASKS_COMPLETED]: Completed alert rules, runbook documentation, SLO configuration, grading evidence checklist, and final team report assembly.
- [EVIDENCE_LINK]: [evidence/alert-rules.png](evidence/alert-rules.png)
- [RUNBOOK_EVIDENCE]: [evidence/alert-doc.png](evidence/alert-doc.png)

---

## 6. Bonus Items (Optional)

- [BONUS_COST_OPTIMIZATION]: N/A
- [BONUS_AUDIT_LOGS]: N/A
- [BONUS_CUSTOM_METRIC]: N/A
