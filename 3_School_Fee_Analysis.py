import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💳 School Fee Payment & Default Analysis")

@st.cache_data
def generate_data():
    import numpy as np
    data = {
        "Student_ID": [f"S{i:03d}" for i in range(1, 201)],
        "Amount_Due": np.random.randint(50000, 100000, 200),
        "Amount_Paid": np.random.randint(30000, 100000, 200),
        "Department": np.random.choice(["Computer Science", "Engineering", "Accounting", "Economics"], 200)
    }
    df = pd.DataFrame(data)
    df["Outstanding"] = df["Amount_Due"] - df["Amount_Paid"]
    df["Status"] = df["Outstanding"].apply(lambda x: "Defaulter" if x > 0 else "Cleared")
    return df

df = generate_data()
st.write(df.head())

fig = px.pie(df, names="Status", title="Payment Status Distribution")
st.plotly_chart(fig, use_container_width=True)

fig2 = px.bar(df, x="Department", y="Outstanding", color="Status", title="Outstanding Fees by Department")
st.plotly_chart(fig2, use_container_width=True)
