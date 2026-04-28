import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Student Score Predictor", page_icon="🎓")

st.title("🎓 Student Math Score Prediction")
st.write("Enter student details to predict the Math Score")

# ----------------------------
# Sample Training Data
# ----------------------------
data = pd.DataFrame({
    "gender": ["male", "female", "male", "female", "male", "female"],
    "race/ethnicity": ["group A", "group B", "group C", "group D", "group E", "group A"],
    "parental level of education": [
        "high school",
        "bachelor's degree",
        "some college",
        "master's degree",
        "associate's degree",
        "some high school"
    ],
    "lunch": ["standard", "free/reduced", "standard", "standard", "free/reduced", "standard"],
    "test preparation course": ["none", "completed", "completed", "none", "completed", "none"],
    "reading score": [72, 90, 65, 88, 76, 60],
    "writing score": [70, 95, 63, 90, 78, 58],
    "math score": [68, 92, 64, 89, 80, 55]
})

# ----------------------------
# Convert Categorical Data
# ----------------------------
X = data.drop("math score", axis=1)
y = data["math score"]

X = pd.get_dummies(X)

# ----------------------------
# Train Model Directly
# ----------------------------
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# ----------------------------
# User Inputs
# ----------------------------
gender = st.selectbox("Gender", ["male", "female"])

race = st.selectbox(
    "Race / Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)

parent_edu = st.selectbox(
    "Parental Education",
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

prep = st.selectbox("Test Preparation Course", ["none", "completed"])

reading = st.slider("Reading Score", 0, 100, 50)
writing = st.slider("Writing Score", 0, 100, 50)

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict Math Score"):

    input_data = pd.DataFrame([{
        "gender": gender,
        "race/ethnicity": race,
        "parental level of education": parent_edu,
        "lunch": lunch,
        "test preparation course": prep,
        "reading score": reading,
        "writing score": writing
    }])

    input_data = pd.get_dummies(input_data)
    input_data = input_data.reindex(columns=X.columns, fill_value=0)

    prediction = model.predict(input_data)[0]

    st.success(f"📘 Predicted Math Score: {prediction:.2f}")
