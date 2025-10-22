import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Sales Forecasting Dashboard")

uploaded_file = st.sidebar.file_uploader("Upload Sales Dataset (CSV)", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file, encoding='ISO-8859-1', parse_dates=True)

    st.write("### Preview Data", df.head())

    date_col = st.selectbox("Select Date Column", df.columns)
    sales_col = st.selectbox("Select Sales Column", df.columns)

    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.sort_values(by=date_col)

    st.subheader("📊 Sales Trend Over Time")
    plt.figure(figsize=(10, 5))
    plt.plot(df[date_col], df[sales_col])
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.title("Sales Over Time")
    st.pyplot(plt)

    st.subheader("🧾 Summary")
    st.write(df[sales_col].describe())
else:
    st.info("👈 Upload a CSV file to begin your sales analysis.")
