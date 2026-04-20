# Day 13 Team Ownership

## Team

| Member | Role | Primary Scope |
|---|---|---|
| Mai Tan Thanh | Tech Lead / Integration Owner | Logging pipeline, correlation ID, integration, final merge |
| Ho Nhat Khoa | Tracing Owner | Langfuse setup, trace verification, trace evidence |
| Dang Tung Anh | PII Owner | PII scrub patterns, tests, log leak verification |
| Nguyen Duc Hoang Phuc | Metrics & Dashboard Owner | Metrics checks, load test, dashboard panels, incident evidence |
| Pham Le Hoang Nam | Alerts & Report Owner | SLOs, alert rules, runbook links, blueprint report |

## Working Rule

1. Mai Tan Thanh creates the starter branch and merges final integration changes.
2. Each member works on a separate branch from the starter commit.
3. Each member owns the files listed below and should avoid editing files owned by others unless integration requires it.
4. If a cross-file change is needed, the file owner reviews it before merge.
5. Every member must keep at least one clear commit for individual evidence.

## File Ownership

### Mai Tan Thanh
- `app/middleware.py`
- `app/main.py`
- `app/logging_config.py`
- final integration checks with `scripts/validate_logs.py`

### Ho Nhat Khoa
- `app/tracing.py`
- trace verification in `app/agent.py`
- `.env` setup for Langfuse on local machine
- evidence from Langfuse UI

### Dang Tung Anh
- `app/pii.py`
- `tests/test_pii.py`
- log leak verification using `data/sample_queries.jsonl`

### Nguyen Duc Hoang Phuc
- `app/metrics.py`
- `scripts/load_test.py`
- dashboard build from `/metrics`
- incident test flow with `scripts/inject_incident.py`

### Pham Le Hoang Nam
- `config/slo.yaml`
- `config/alert_rules.yaml`
- `docs/alerts.md`
- `docs/blueprint-template.md`
- `docs/grading-evidence.md`

## Deliverables By Owner

### Mai Tan Thanh
- correlation ID works end-to-end
- API logs contain `user_id_hash`, `session_id`, `feature`, `model`, `env`
- response headers include request id and response time

### Ho Nhat Khoa
- at least 10 traces visible in Langfuse
- one trace waterfall screenshot
- trace metadata shows user/session/tags

### Dang Tung Anh
- logs do not expose email, phone, CCCD, or credit card values
- tests for main PII patterns pass
- sample leak evidence before/after can be explained

### Nguyen Duc Hoang Phuc
- dashboard has 6 required panels
- load test produces enough data for charts
- incident scenarios can be demonstrated with metrics

### Pham Le Hoang Nam
- alert rules point to valid runbook links
- SLO table is filled with final values
- final blueprint report is complete

## Suggested Branch Names

- `mtt/logging-integration`
- `khoa/tracing`
- `anh/pii`
- `phuc/metrics-dashboard`
- `nam/alerts-report`

## Starter Workflow

1. Push this starter repo to the new group repository.
2. Ask everyone to clone and create their branch immediately.
3. Mai Tan Thanh completes the integration baseline first.
4. Other members work in parallel on their owned files.
5. Merge in this order: PII -> tracing -> metrics/dashboard -> alerts/report -> final integration.
