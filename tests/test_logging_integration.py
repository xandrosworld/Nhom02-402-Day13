import json
from pathlib import Path

from fastapi.testclient import TestClient

import app.logging_config as logging_config
import app.main as main_module
from app.agent import AgentResult
from app.pii import hash_user_id


def _stub_result() -> AgentResult:
    return AgentResult(
        answer="Stubbed answer",
        latency_ms=123,
        tokens_in=10,
        tokens_out=20,
        cost_usd=0.001,
        quality_score=0.9,
    )


def test_chat_generates_request_id_and_response_time_headers(monkeypatch) -> None:
    monkeypatch.setattr(main_module.agent, "run", lambda **_: _stub_result())

    with TestClient(main_module.app) as client:
        response = client.post(
            "/chat",
            json={
                "user_id": "u01",
                "session_id": "s01",
                "feature": "qa",
                "message": "What is the policy?",
            },
        )

    assert response.status_code == 200
    assert response.headers["x-request-id"].startswith("req-")
    assert response.headers["x-response-time-ms"].isdigit()
    assert response.json()["correlation_id"] == response.headers["x-request-id"]


def test_chat_reuses_incoming_request_id_and_writes_enriched_logs(tmp_path: Path, monkeypatch) -> None:
    log_path = tmp_path / "logs.jsonl"

    monkeypatch.setattr(main_module.agent, "run", lambda **_: _stub_result())
    monkeypatch.setattr(logging_config, "LOG_PATH", log_path)
    monkeypatch.setenv("APP_ENV", "test")

    with TestClient(main_module.app) as client:
        response = client.post(
            "/chat",
            headers={"x-request-id": "req-fixed123"},
            json={
                "user_id": "u99",
                "session_id": "s99",
                "feature": "summary",
                "message": "My email is student@vinuni.edu.vn",
            },
        )

    assert response.status_code == 200
    assert response.headers["x-request-id"] == "req-fixed123"

    records = [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    api_records = [record for record in records if record.get("service") == "api"]

    assert {record["event"] for record in api_records} == {"request_received", "response_sent"}
    assert all(record["correlation_id"] == "req-fixed123" for record in api_records)
    assert all(record["session_id"] == "s99" for record in api_records)
    assert all(record["feature"] == "summary" for record in api_records)
    assert all(record["model"] == main_module.agent.model for record in api_records)
    assert all(record["env"] == "test" for record in api_records)
    assert all(record["user_id_hash"] == hash_user_id("u99") for record in api_records)
