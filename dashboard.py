import streamlit as st
import pandas as pd

st.title("Dark Web & Threat Intelligence Dashboard")

# Load CSV
df = pd.read_csv("darkweb_alerts.csv")

if df.empty:
    st.warning("No alerts detected!")
else:
    st.subheader("Alerts Table")
    st.dataframe(df)

    st.subheader("Keyword Frequency")
    st.bar_chart(df['keyword'].value_counts())
