import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title("⭐ Lecturer & Course Evaluation Insights")

@st.cache_data
def generate_evaluation():
    lecturers = [f"Dr. {name}" for name in ["Johnson","Okon","Williams","Udo","Emeka","Ibrahim"]]
    courses = ["Data Science", "Accounting", "Marketing", "AI Systems", "Engineering Math", "Database Systems"]
    df = pd.DataFrame({
        "Lecturer": np.random.choice(lecturers, 150),
        "Course": np.random.choice(courses, 150),
        "Clarity": np.random.randint(50, 100, 150),
        "Engagement": np.random.randint(40, 100, 150),
        "Fairness": np.random.randint(50, 100, 150)
    })
    df["Average Rating"] = df[["Clarity","Engagement","Fairness"]].mean(axis=1)
    return df

df = generate_evaluation()

st.subheader("📋 Sample Evaluations")
st.write(df.head())

fig = px.bar(df.groupby("Lecturer")["Average Rating"].mean().reset_index(),
             x="Lecturer", y="Average Rating", color="Average Rating",
             title="Average Lecturer Ratings")
st.plotly_chart(fig, use_container_width=True)

fig2 = px.box(df, x="Course", y="Average Rating", color="Course", title="Course Evaluation Distribution")
st.plotly_chart(fig2, use_container_width=True)
