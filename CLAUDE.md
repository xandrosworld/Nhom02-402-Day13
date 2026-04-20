# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a FastAPI-based observability lab (Day 13) for a team of 5 students learning structured logging, distributed tracing, PII scrubbing, and metrics instrumentation on an AI/RAG agent simulation.

## Setup & Commands

```bash
# Setup
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env             # Fill in Langfuse credentials

# Run (with hot reload)
uvicorn app.main:app --reload

# Tests
python -m pytest tests/
python -m pytest tests/test_pii.py   # Single test file

# Validation & load testing
python scripts/validate_logs.py      # Primary grading tool (scores 0-100)
python scripts/load_test.py --concurrency 5
python scripts/inject_incident.py --scenario rag_slow
```

## Architecture

**Request flow:**
1. HTTP request → `CorrelationIdMiddleware` (`app/middleware.py`) generates/propagates `correlation_id` via structlog contextvars
2. `/chat` endpoint (`app/main.py`) calls `LabAgent.run()` (`app/agent.py`)
3. `LabAgent` runs a 4-step RAG pipeline: retrieve → prompt → generate (mock LLM) → quality score
4. Every request records metrics via `app/metrics.py` and emits structured JSON logs via `app/logging_config.py`
5. Langfuse tracing wraps `agent.run()` via `@observe()` from `app/tracing.py`

**Key modules:**
- `app/logging_config.py` — structlog pipeline ending in `JsonlFileProcessor` that appends to `data/logs.jsonl`; PII scrubbing runs as a processor via `app/pii.py`
- `app/pii.py` — regex-based scrubbing for email, VN phone, CCCD (12-digit), credit card, passport, VN address; replaces with `[REDACTED_{TYPE}]`; SHA256-hashes user IDs
- `app/tracing.py` — lazy Langfuse init with fallback no-ops when credentials absent
- `app/metrics.py` — in-memory lists for latency/cost/tokens/quality; `snapshot()` computes P50/P95/P99
- `app/incidents.py` — toggles for chaos scenarios (`rag_slow`, `tool_fail`, `cost_spike`) used by mock components

**Endpoints:**
| Method | Path | Purpose |
|--------|------|---------|
| POST | `/chat` | Main agent endpoint |
| GET | `/health` | Health + tracing status |
| GET | `/metrics` | Live metrics snapshot |
| POST | `/incidents/{name}/enable` | Enable chaos scenario |
| POST | `/incidents/{name}/disable` | Disable chaos scenario |

## Validation & Grading

`scripts/validate_logs.py` parses `data/logs.jsonl` and scores:
- 30pts: Required fields (`ts`, `level`, `event`, `correlation_id`)
- 20pts: Correlation ID propagation (unique per request)
- 20pts: Enrichment fields (`user_id_hash`, `session_id`, `feature`, `model`)
- 30pts: No PII leaks (`@` symbols or `4111` test card numbers in raw log JSON)

Pass threshold: **80/100**.

## Configuration

- `config/slo.yaml` — SLO targets (P95 latency 3000ms, error rate 2%, cost $2.5/day, quality 0.75)
- `config/alert_rules.yaml` — 6 alert rules with severity and runbook references
- `docs/alerts.md` — Runbook for all 6 alert types
- Environment variables: `APP_ENV`, `LOG_LEVEL`, `LOG_PATH`, `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`

## Team File Ownership (see TEAM_OWNERSHIP.md)

| Member | Files |
|--------|-------|
| Mai Tan Thanh | `app/main.py`, `app/logging_config.py`, `app/middleware.py` |
| Dang Tung Anh | `app/pii.py`, `tests/test_pii.py` |
| Ho Nhat Khoa | `app/tracing.py` |
| Nguyen Duc Hoang Phuc | `app/metrics.py` |
| Nam | `config/slo.yaml`, `config/alert_rules.yaml`, `docs/alerts.md` |

## Deliverables

Required evidence screenshots belong in `docs/evidence/`: `correlation-id.png`, `trace-list.png`, `trace-waterfall.png`, `pii-redaction.png`, `dashboard-6-panels.png`, `alert-rules.png`, `incident-before-after.png`.

Team submission report: `docs/blueprint-template.md`.
