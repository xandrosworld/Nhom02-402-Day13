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
