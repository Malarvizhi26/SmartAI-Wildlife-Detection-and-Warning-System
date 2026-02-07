import streamlit as st
import pandas as pd
from database import get_all_alerts, get_stats, init_db
import plotly.express as px
import plotly.graph_objects as go

# Initialize database
init_db()

# Page config
st.set_page_config(page_title="Wildlife Detection Dashboard", page_icon="🦁", layout="wide")

# Title
st.title("🦁 Smart AI Wildlife Detection Dashboard")
st.markdown("---")

# Refresh button
if st.button("🔄 Refresh Data"):
    st.rerun()

# Get statistics
stats = get_stats()

# Top metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Alerts", stats["total"])
with col2:
    st.metric("Emails Sent", stats["emails_sent"])
with col3:
    success_rate = (stats["emails_sent"] / stats["total"] * 100) if stats["total"] > 0 else 0
    st.metric("Email Success Rate", f"{success_rate:.1f}%")

st.markdown("---")

# Charts
if stats["by_animal"]:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Detections by Animal")
        df_animals = pd.DataFrame(stats["by_animal"], columns=["Animal", "Count"])
        fig = px.bar(df_animals, x="Animal", y="Count", color="Animal")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🥧 Animal Distribution")
        fig = px.pie(df_animals, values="Count", names="Animal")
        st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# Alerts table
st.subheader("📋 Recent Alerts")

alerts = get_all_alerts()

if alerts:
    df = pd.DataFrame(alerts, columns=["ID", "Animal", "Confidence", "Timestamp", "Email Sent"])
    df["Email Sent"] = df["Email Sent"].apply(lambda x: "✅" if x == 1 else "❌")
    df["Confidence"] = df["Confidence"].apply(lambda x: f"{x:.2%}")
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        animal_filter = st.multiselect("Filter by Animal", options=df["Animal"].unique())
    with col2:
        email_filter = st.selectbox("Email Status", ["All", "Sent ✅", "Failed ❌"])
    
    # Apply filters
    filtered_df = df.copy()
    if animal_filter:
        filtered_df = filtered_df[filtered_df["Animal"].isin(animal_filter)]
    if email_filter == "Sent ✅":
        filtered_df = filtered_df[filtered_df["Email Sent"] == "✅"]
    elif email_filter == "Failed ❌":
        filtered_df = filtered_df[filtered_df["Email Sent"] == "❌"]
    
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    
    # Download button
    csv = filtered_df.to_csv(index=False)
    st.download_button("📥 Download CSV", csv, "wildlife_alerts.csv", "text/csv")
else:
    st.info("No alerts recorded yet. Start the detection system to see data.")

# Sidebar
with st.sidebar:
    st.header("⚙️ System Info")
    st.info("Detection system must be running separately (app.py)")
    
    st.markdown("---")
    st.header("📖 Instructions")
    st.markdown("""
    1. Run `app.py` to start detection
    2. Configure email in `config.py`
    3. View alerts here in real-time
    4. Use filters to analyze data
    """)
    
    st.markdown("---")
    st.header("🔔 Alert Settings")
    if st.button("Clear All Alerts"):
        st.warning("Feature coming soon!")
