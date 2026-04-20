# dashboard.py
import requests
import streamlit as st

data = requests.get("http://localhost:8000/metrics").json()

st.title("AI System Dashboard")

st.metric("Traffic", data["traffic"])
st.metric("Latency P50", data["latency_p50"])
st.metric("Latency P95", data["latency_p95"])
st.metric("Latency P99", data["latency_p99"])

st.metric("Avg Cost", data["avg_cost_usd"])
st.metric("Total Cost", data["total_cost_usd"])

st.metric("Tokens In", data["tokens_in_total"])
st.metric("Tokens Out", data["tokens_out_total"])

st.metric("Quality", data["quality_avg"])