import streamlit as st
import requests
import pandas as pd
import time
import os

API = os.getenv("API_BASE_URL", "http://api:8000")

st.title("DevOps Monitoring Dashboard")

tab1, tab2 = st.tabs(["Metrics", "Servers"])


# ---------------- METRICS ----------------
with tab1:
    st.header("System Metrics")

    placeholder = st.empty()

    for _ in range(60):
        try:
            data = requests.get(f"{API}/metrics").json()
        except:
            data = {"cpu_percent": 0, "memory_percent": 0, "disk_percent": 0}

        with placeholder.container():
            st.metric("CPU %", data["cpu_percent"])
            st.metric("Memory %", data["memory_percent"])
            st.metric("Disk %", data["disk_percent"])

        time.sleep(1)
        st.rerun()


# ---------------- SERVERS ----------------
with tab2:
    st.header("Servers")

    try:
        servers = requests.get(f"{API}/servers").json()
    except:
        servers = []

    df = pd.DataFrame(servers)

    def color_status(val):
        if val == "UP":
            return "background-color: green"
        if val == "DEGRADED":
            return "background-color: orange"
        if val == "DOWN":
            return "background-color: red"
        return ""

    if not df.empty:
        st.dataframe(df.style.applymap(color_status, subset=["status"]))

    st.subheader("Add server")

    with st.form("add"):
        name = st.text_input("Name")
        host = st.text_input("Host")
        port = st.number_input("Port", 1, 65535, 443)
        protocol = st.selectbox("Protocol", ["http", "https"])
        path = st.text_input("Health path")

        submitted = st.form_submit_button("Add")

        if submitted:
            requests.post(
                f"{API}/servers",
                json={
                    "name": name,
                    "host": host,
                    "port": port,
                    "protocol": protocol,
                    "health_path": path,
                },
                headers={"X-API-Key": os.getenv("API_KEY", "")},
            )
            st.rerun()
