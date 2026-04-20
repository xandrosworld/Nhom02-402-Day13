# Owner: Pham Le Hoang Nam

# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata

- [GROUP_NAME]\: Nhom02-402-Day13
- [REPO_URL]\: https://github.com/xandrosworld/Nhom02-402-Day13
- [MEMBERS]\:
  - Member A: Mai Táº¥n ThÃ nh | Role: Tech Lead / Integration Owner
  - Member B: Há»“ Nháº¥t Khoa | Role: Tracing Owner
  - Member C: Äáº·ng TÃ¹ng Anh | Role: PII Owner
  - Member D: Nguyá»…n Äá»©c HoÃ ng PhÃºc | Role: Metrics & Dashboard Owner
  - Member E: Pháº¡m LÃª HoÃ ng Nam | Role: Alerts & Report Owner

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

### Mai Táº¥n ThÃ nh

- [TASKS_COMPLETED]\: TÃ­ch há»£p middleware xá»­ lÃ½ sinh vÃ  truyá»n `correlation_id` (vd: `req-da313bf8`). Bind Ä‘áº§y Ä‘á»§ cÃ¡c tag ngá»¯ cáº£nh (`user_id_hash`, `session_id`, `feature`, `model`, `env`) vÃ o cáº¥u trÃºc log.
- [EVIDENCE_LINK]\: [evidence/correlation-id.png](evidence/correlation-id.png)

### Há»“ Nháº¥t Khoa

- [TASKS_COMPLETED]\: Triá»ƒn khai toÃ n bá»™ Langfuse tracing integration trong `app/tracing.py`. Cá»¥ thá»ƒ: (1) lazy initialization vá»›i `get_client()` vÃ  graceful fallback no-ops khi thiáº¿u credentials, Ä‘áº£m báº£o app cháº¡y Ä‘Æ°á»£c cáº£ khi khÃ´ng cÃ³ Langfuse; (2) export `observe()` decorator Ä‘Æ°á»£c Ã¡p dá»¥ng trá»±c tiáº¿p lÃªn `LabAgent.run()` trong `app/agent.py`, táº¡o trace span bao toÃ n bá»™ pipeline RAG; (3) `update_current_trace()` gáº¯n `user_id` Ä‘Ã£ hash SHA256, `session_id`, vÃ  tags `["lab", feature, model]` vÃ o má»—i trace; (4) `update_current_observation()` gáº¯n metadata `doc_count`, `query_preview` (Ä‘Ã£ scrub PII), `input`, `output` vÃ o span; (5) `tracing_enabled()` Ä‘Æ°á»£c dÃ¹ng bá»Ÿi `/health` endpoint Ä‘á»ƒ bÃ¡o cÃ¡o tráº¡ng thÃ¡i Langfuse; (6) setup `LANGFUSE_BASE_URL` tá»± Ä‘á»™ng tá»« `LANGFUSE_HOST` Ä‘á»ƒ tÆ°Æ¡ng thÃ­ch cáº£ self-hosted láº«n cloud.
- [EVIDENCE_LINK]\: [evidence/trace-list.png](evidence/trace-list.png) | [evidence/trace-waterfall.png](evidence/trace-waterfall.png)

### Äáº·ng TÃ¹ng Anh

- [TASKS_COMPLETED]\: ÄÃ£ áº©n vÃ  mÃ£ hÃ³a thÃ nh cÃ´ng email, tháº» tÃ­n dá»¥ng (`[REDACTED_CREDIT_CARD]`), CCCD (`[REDACTED_CCCD]`), Sá»‘ Ä‘iá»‡n thoáº¡i khu vá»±c VN (`[REDACTED_PHONE_VN]`), cÅ©ng nhÆ° add thÃªm cá»¥m tá»« khÃ³a báº¯t Há»™ chiáº¿u (Passport) vÃ  Äá»‹a chá»‰ nhÃ .
- [EVIDENCE_LINK]\: [evidence/pii-redaction.png](evidence/pii-redaction.png)

### Nguyá»…n Äá»©c HoÃ ng PhÃºc

- [TASKS_COMPLETED]\:
- [EVIDENCE_LINK]\:

### Pháº¡m LÃª HoÃ ng Nam

- [TASKS_COMPLETED]\: Cáº¥u hÃ¬nh 6 cáº£nh bÃ¡o má»©c P1-P3 trong `config/alert_rules.yaml`, biÃªn soáº¡n runbook xá»­ lÃ½ sá»± cá»‘ trong `docs/alerts.md`, thiáº¿t láº­p thÃ´ng sá»‘ cho `config/slo.yaml`, vÃ  tá»•ng há»£p hoÃ n thiá»‡n bÃ¡o cÃ¡o Lab (Blueprint + Grading Evidence).
- [EVIDENCE_LINK]\: [evidence/alert-rules.png](evidence/alert-rules.png)
- [RUNBOOK_EVIDENCE]\: [evidence/alert-doc.png](evidence/alert-doc.png)

---

## 6. Bonus Items (Optional)

- [BONUS_COST_OPTIMIZATION]\: (Description + Evidence)
- [BONUS_AUDIT_LOGS]\: (Description + Evidence)
- [BONUS_CUSTOM_METRIC]\: (Description + Evidence)
