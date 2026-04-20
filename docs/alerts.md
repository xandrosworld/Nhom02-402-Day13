# Owner: Pham Le Hoang Nam

# Alert Rules and Runbooks

## 1. High latency P95

- Severity: P2
- Trigger: `latency_p95_ms > 5000 for 30m`
- Impact: tail latency breaches SLO
- First checks:
  1. Check the [Observability Dashboard](dashboard-spec.md) for top slow traces in the last 1h
  2. Compare RAG span vs LLM span
  3. Check if incident toggle `rag_slow` is enabled
- Mitigation:
  - truncate long queries
  - fallback retrieval source
  - lower prompt size

## 2. High error rate

- Severity: P1
- Trigger: `error_rate_pct > 5 for 5m`
- Impact: users receive failed responses
- First checks:
  1. Group logs in [logs.jsonl](../data/logs.jsonl) by `error_type`
  2. Inspect failed traces
  3. Determine whether failures are LLM, tool, or schema related
- Mitigation:
  - rollback latest change
  - disable failing tool
  - retry with fallback model

## 3. Cost budget spike

- Severity: P2
- Trigger: `hourly_cost_usd > 0.5 for 15m`
- Impact: burn rate exceeds budget
- First checks:
  1. Check the [Observability Dashboard](dashboard-spec.md) to split traces by feature and model
  2. Compare tokens_in/tokens_out
  3. Check if `cost_spike` incident was enabled
- Mitigation:
  - shorten prompts
  - route easy requests to cheaper model
  - apply prompt cache

## 4. Quality score drop

- Severity: P3
- Trigger: `quality_score_avg < 0.75 for 1h`
- Impact: degraded AI response quality and user satisfaction
- First checks:
  1. Filter [audit.jsonl](../data/audit.jsonl) or Langfuse dashboard for negative feedbacks.
  2. Evaluate latest prompt or agent pipeline changes.
- Mitigation:
  - rollback prompt version
  - escalate to AI engineers for instruction tuning

## 5. Traffic spike detected

- Severity: P3
- Trigger: `requests_per_min > 500 for 5m`
- Impact: high load on infrastructure and APIs, risk of rate-limiting by LLM providers.
- First checks:
  1. Check the [Observability Dashboard](dashboard-spec.md) for "Active Sessions" and "Request Volume" panels.
  2. Identify if the traffic is legitimate or malicious (e.g., from a single IP/User).
- Mitigation:
  - scale out replicas
  - apply API rate limiting to aggressive IPs
  - notify LLM provider to increase quota if legitimate

## 6. PII redaction anomaly

- Severity: P2
- Trigger: `pii_redact_rate > 20 for 10m`
- Impact: potential security risk, malicious intent to prompt-inject sensitive data, or overhead in the redaction pipeline.
- First checks:
  1. Review logs in [logs.jsonl](../data/logs.jsonl) for redacted PII patterns (email, phone, credit card).
  2. Check which users/sessions are sending the most PII.
- Mitigation:
  - block or rate-limit suspicious user IDs
  - review PII scrubbing logic in `app/pii.py` for false positives
