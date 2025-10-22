import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("🎓 Student Performance & Risk Analysis")

@st.cache_data
def load_data():
    return pd.read_csv("data/Student_Performance.csv")

df = load_data()

st.subheader("📋 Dataset Preview")
st.write(df.head())

st.subheader("📊 Department Distribution")
fig = px.histogram(df, x="Department", color="At_Risk", barmode="group")
st.plotly_chart(fig, use_container_width=True)

st.subheader("📈 Performance Trend by Department")
dept_perf = df.groupby("Department")[["Assignment Score","Test Score","Exam Score"]].mean().reset_index()
fig2 = px.bar(dept_perf, x="Department", y=["Assignment Score","Test Score","Exam Score"], barmode="group")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("⚠️ Risk Distribution")
risk_count = df["At_Risk"].value_counts()
st.bar_chart(risk_count)

st.subheader("🧾 Summary Statistics")
st.write(df.describe())
