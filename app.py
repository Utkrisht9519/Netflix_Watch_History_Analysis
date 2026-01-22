import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Netflix BI Dashboard", layout="wide")

st.title("Netflix Watch History BI Dashboard")

# Load dataset
df = pd.read_csv("BI&A - Tableau Quiz Dataset - For Candidates.csv")

# ---------------- Chart 1 ----------------
st.subheader("Total Watch Time by Subscription Type")
watch_time = df.groupby('subscription_type')['duration_watched(minutes)'].sum()
st.bar_chart(watch_time)

# ---------------- Chart 2 ----------------
st.subheader("Average Watch Time by Device")
avg_watch = df.groupby('device_used')['duration_watched(minutes)'].mean()
st.bar_chart(avg_watch)

# ---------------- Chart 3 ----------------
st.subheader("Viewing Frequency per User")
views = df.groupby('user_id')['date_watched'].count()
st.bar_chart(views.value_counts())
