from __future__ import annotations

import os

import httpx
import streamlit as st

METRICS_URL = os.getenv("METRICS_URL", "http://127.0.0.1:8000/metrics")

st.set_page_config(page_title="Day 13 Dashboard", layout="wide")
st.title("AI System Dashboard")
st.caption(f"Metrics source: {METRICS_URL}")

try:
    response = httpx.get(METRICS_URL, timeout=10.0)
    response.raise_for_status()
    data = response.json()
except Exception as exc:
    st.error(f"Khong the tai metrics tu {METRICS_URL}: {exc}")
    st.stop()

latency_col, traffic_col, error_col = st.columns(3)
latency_col.metric("Latency P50", data["latency_p50"])
traffic_col.metric("Traffic", data["traffic"])
error_col.metric("Error Types", len(data["error_breakdown"]))

latency95_col, latency99_col, cost_col = st.columns(3)
latency95_col.metric("Latency P95", data["latency_p95"])
latency99_col.metric("Latency P99", data["latency_p99"])
cost_col.metric("Total Cost", data["total_cost_usd"])

token_in_col, token_out_col, quality_col = st.columns(3)
token_in_col.metric("Tokens In", data["tokens_in_total"])
token_out_col.metric("Tokens Out", data["tokens_out_total"])
quality_col.metric("Quality", data["quality_avg"])

st.subheader("Error Breakdown")
st.json(data["error_breakdown"])
