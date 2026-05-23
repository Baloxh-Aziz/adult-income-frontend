import streamlit as st
import requests
import pandas as pd

st.title("Income Classification System")
st.write("Enter individual details to predict if income exceeds $50K/year.")

API_URL = "https://hacker-ai-backend-ml-project.hf.space/predict"

df = pd.read_csv("adult.csv")

workclass_options      = sorted(df["workclass"].dropna().unique().tolist())
education_options      = sorted(df["education"].dropna().unique().tolist())
marital_options        = sorted(df["marital-status"].dropna().unique().tolist())
occupation_options     = sorted(df["occupation"].dropna().unique().tolist())
relationship_options   = sorted(df["relationship"].dropna().unique().tolist())
race_options           = sorted(df["race"].dropna().unique().tolist())
gender_options         = sorted(df["gender"].dropna().unique().tolist())
native_country_options = sorted(df["native-country"].dropna().unique().tolist())
# ─────────────────────────────────────────────────────────────────

with st.form("input_form"):
    age             = st.number_input("Age", min_value=17, max_value=100, value=30)
    workclass       = st.selectbox("Workclass", workclass_options)
    fnlwgt          = st.number_input("Final Weight (fnlwgt)", min_value=10000, value=100000)
    education       = st.selectbox("Education", education_options)
    educational_num = st.number_input("Educational Num", min_value=1, max_value=16, value=10)
    marital_status  = st.selectbox("Marital Status", marital_options)
    occupation      = st.selectbox("Occupation", occupation_options)
    relationship    = st.selectbox("Relationship", relationship_options)
    race            = st.selectbox("Race", race_options)
    gender          = st.selectbox("Gender", gender_options)
    capital_gain    = st.number_input("Capital Gain", min_value=0, value=0)
    capital_loss    = st.number_input("Capital Loss", min_value=0, value=0)
    hours_per_week  = st.number_input("Hours Per Week", min_value=1, max_value=100, value=40)
    native_country  = st.selectbox("Native Country", native_country_options)

    submit_button = st.form_submit_button("Predict Income")

if submit_button:
    payload = {
        "age": age,
        "workclass": workclass,
        "fnlwgt": fnlwgt,
        "education": education,
        "educational_num": educational_num,
        "marital_status": marital_status,
        "occupation": occupation,
        "relationship": relationship,
        "race": race,
        "gender": gender,
        "capital_gain": capital_gain,
        "capital_loss": capital_loss,
        "hours_per_week": hours_per_week,
        "native_country": native_country
    }

    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            result = response.json()
            bracket = result["income_prediction"]

            if bracket == ">50K":
                st.success(f"Prediction: High Income Bracket ({bracket})")
            else:
                st.success(f"Prediction: Low Income Bracket ({bracket})")
        else:
            st.error("Error occurred in API side.")
    except Exception as e:
        st.error(f"Could not connect to backend API: {e}")