import streamlit as st
import random
import time
from datetime import datetime

def get_random_metrics():
    return {
        "Throughput": f"{random.uniform(0, 100):.2f} MB/s",
        "Latency": f"{random.randint(0, 100)} ms",
        "Success Rate": f"{random.uniform(90, 100):.2f}%",
        "Active Workers": f"{random.randint(5, 15)}"
    }

def get_pipeline_status():
    components = [
        {"name": "AWS S3", "status": "operational"},
        {"name": "AWS Kinesis", "status": "operational"},
        {"name": "AWS Lambda", "status": "operational"},
        {"name": "Apache Kafka", "status": "operational"},
        {"name": "Apache Spark", "status": "operational"}
    ]
    return components

st.set_page_config(page_title="Real-Time Data Pipeline Dashboard", layout="wide")

st.title("🚀 Real-Time Data Pipeline Dashboard")

# Navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("### Status: ✅ Processing Active")

# Metrics Overview
st.subheader("📊 Metrics Overview")
metrics_placeholder = st.empty()

# Pipeline Status
st.subheader("🔄 Pipeline Components Status")
status_placeholder = st.empty()

# Real-time Logs
st.subheader("📜 Real-time Logs")
log_container = st.empty()

log_messages = []

def add_log():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    messages = [
        "Processing batch of records...",
        "Data transformation completed successfully",
        "Scaling up workers to handle increased load",
        "Successfully integrated with external systems",
        "Optimizing performance metrics"
    ]
    return f"[{timestamp}] {random.choice(messages)}"

# Real-time updates
while True:
    metrics = get_random_metrics()
    components = get_pipeline_status()
    
    with metrics_placeholder.container():
        cols = st.columns(4)
        for idx, (key, value) in enumerate(metrics.items()):
            with cols[idx]:
                st.metric(label=key, value=value)
    
    with status_placeholder.container():
        for component in components:
            st.write(f"**{component['name']}** - ✅ {component['status'].capitalize()}")
    
    log_messages.insert(0, add_log())
    if len(log_messages) > 50:
        log_messages.pop()
    
    log_container.text("\n".join(log_messages))
    
    time.sleep(3)
