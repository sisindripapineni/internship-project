import streamlit as st
import pandas as pd
import pickle
import os

# Page settings
st.set_page_config(page_title="Student Score Predictor", page_icon="🎓", layout="centered")

# Title
st.title("🎓 Student Math Score Prediction")
st.write("Enter student details to predict the Math Score.")

# Get current folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "student_model.pkl")

# Check model file exists
if not os.path.exists(model_path):
    st.error("❌ student_model.pkl file not found!")
    st.info("Make sure student_model.pkl is in the same folder as this Python file.")
    st.stop()

# Load model
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Input fields
gender = st.selectbox("Gender", ["male", "female"])

race_ethnicity = st.selectbox(
    "Race / Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)

parent_edu = st.selectbox(
    "Parental Level of Education",
    [
        "some high school",
        "high school",
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree"
    ]
)

lunch = st.selectbox("Lunch", ["standard", "free/reduced"])

test_prep = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)

reading_score = st.slider("Reading Score", 0, 100, 50)
writing_score = st.slider("Writing Score", 0, 100, 50)

# Prediction button
if st.button("Predict Math Score"):

    input_data = pd.DataFrame([{
        "gender": gender,
        "race/ethnicity": race_ethnicity,
        "parental level of education": parent_edu,
        "lunch": lunch,
        "test preparation course": test_prep,
        "reading score": reading_score,
        "writing score": writing_score
    }])

    try:
        prediction = model.predict(input_data)[0]
        st.success(f"📘 Predicted Math Score: {prediction:.2f}")
    except Exception as e:
        st.error("⚠️ Prediction failed. Check model training columns.")
        st.write(e)
