import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Student Performance Prediction System",
    page_icon="",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
data = pd.read_csv("data.csv")

X = data.drop(["Student_Name", "Final_Score"], axis=1)
y = data["Final_Score"]

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# ---------------- HEADER ----------------
st.markdown(
    """
    <h1 style="text-align:center;">Student Performance Prediction Dashboard</h1>
    <p style="text-align:center; color:gray;">
    AI-powered real-world academic analytics system
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- SIDEBAR ----------------
st.sidebar.header(" Student Details")

student_name = st.sidebar.text_input("Student Name", "Hariom Patidar")
study_hours = st.sidebar.slider("Study Hours (per week)", 1, 20, 6)
attendance = st.sidebar.slider("Attendance (%)", 50, 100, 80)
previous_score = st.sidebar.slider("Previous Exam Score", 0, 100, 65)
assignment_score = st.sidebar.slider("Assignment Score", 0, 100, 70)

st.sidebar.markdown("---")
st.sidebar.info("Model: Random Forest Regressor")

# ---------------- MAIN LAYOUT ----------------
col1, col2 = st.columns([2, 1])

# ---- Student Profile ----
with col1:
    st.subheader(" Student Profile")
    st.write(f"**Name:** {student_name}")
    st.write(f"**Study Hours:** {study_hours} hrs/week")
    st.write(f"**Attendance:** {attendance}%")
    st.write(f"**Previous Score:** {previous_score}")
    st.write(f"**Assignment Score:** {assignment_score}")

# ---- Model Use ----
with col2:
    st.subheader(" Model Insights")
    st.success("Random Forest Regressor")
    st.write("✔ Handles complex patterns")
    st.write("✔ High accuracy")
    st.write("✔ Used in real-world analytics")

st.markdown("---")

# ---------------- Prediction ----------------
if st.button("🚀 Predict Performance"):
    input_data = np.array([[study_hours, attendance, previous_score, assignment_score]])
    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    st.metric("Predicted Final Score", f"{prediction:.2f}")

    # Progress Bar
    st.progress(int(prediction))

    # Status Badge
    if prediction < 50:
        st.error(" Performance Level: Poor")
        recommendation = "Focus on fundamentals and regular practice."
    elif prediction < 65:
        st.warning(" Performance Level: Average")
        recommendation = "Increase study hours and assignment consistency."
    elif prediction < 80:
        st.success(" Performance Level: Good")
        recommendation = "Good progress. Maintain consistency."
    else:
        st.success(" Performance Level: Excellent")
        recommendation = "Excellent performance. Keep it up!"

    # Recommendation Section
    st.markdown("### AI Recommendation")
    st.info(recommendation)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; color:gray; font-size:14px;">
    © 2025 Student Performance Prediction System | Built with Streamlit & Machine Learning
    </div>
    """,
    unsafe_allow_html=True
)
