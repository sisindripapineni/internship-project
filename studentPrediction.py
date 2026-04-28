import streamlit as st

# Page settings
st.set_page_config(
    page_title="Student Math Score Prediction",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Math Score Prediction")
st.write("Enter student details to predict the Math Score.")

# Inputs
gender = st.selectbox("Gender", ["male", "female"])

race = st.selectbox(
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

prep = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)

reading = st.slider("Reading Score", 0, 100, 50)
writing = st.slider("Writing Score", 0, 100, 50)

# Predict button
if st.button("Predict Math Score"):

    # Base formula
    prediction = (reading * 0.45) + (writing * 0.45)

    # Adjustments
    if gender == "male":
        prediction += 2

    if prep == "completed":
        prediction += 5

    if lunch == "standard":
        prediction += 3

    if parent_edu in ["bachelor's degree", "master's degree"]:
        prediction += 4

    if race in ["group D", "group E"]:
        prediction += 2

    # Keep score in range
    prediction = max(0, min(100, prediction))

    # Output
    st.success(f"📘 Predicted Math Score: {prediction:.2f}")
