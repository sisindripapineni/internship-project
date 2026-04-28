import streamlit as st
import pandas as pd
import pickle
import os

# Get current file folder path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct model path
model_path = os.path.join(BASE_DIR, "student_model.pkl")

# Load model safely
with open(model_path, "rb") as f:
    model = pickle.load(f)

# Title
st.title("🎓 Student Math Score Prediction")

# Inputs
gender = st.selectbox("Gender", ["male", "female"])

race_ethnicity = st.selectbox(
    "Race/Ethnicity",
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

reading_score = st.number_input(
    "Reading Score",
    min_value=0,
    max_value=100,
    step=1
)

writing_score = st.number_input(
    "Writing Score",
    min_value=0,
    max_value=100,
    step=1
)

# Prediction
if st.button("Predict Math Score"):

    input_df = pd.DataFrame([{
        "gender": gender,
        "race/ethnicity": race_ethnicity,
        "parental level of education": parent_edu,
        "lunch": lunch,
        "test preparation course": test_prep,
        "reading score": reading_score,
        "writing score": writing_score
    }])

    prediction = model.predict(input_df)[0]

    st.success(f"Predicted Math Score: {prediction:.2f}")
