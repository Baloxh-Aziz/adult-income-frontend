from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class IncomeInput(BaseModel):
    age: int
    workclass: str
    fnlwgt: int
    education: str
    educational_num: int
    marital_status: str
    occupation: str
    relationship: str
    race: str
    gender: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: str

@app.get("/")
def home():
    return {"message": "Welcome to Adult Income Prediction API "}

# Prediction API Endpoint
@app.post("/predict")
def predict_income(data: IncomeInput):

    data_dict = {
        "age":             [data.age],
        "workclass":       [data.workclass],
        "fnlwgt":          [data.fnlwgt],
        "education":       [data.education],
        "educational-num": [data.educational_num],
        "marital-status":  [data.marital_status],
        "occupation":      [data.occupation],
        "relationship":    [data.relationship],
        "race":            [data.race],
        "gender":          [data.gender],
        "capital-gain":    [data.capital_gain],
        "capital-loss":    [data.capital_loss],
        "hours-per-week":  [data.hours_per_week],
        "native-country":  [data.native_country],
    }

    # 3. prediction from model
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        income_bracket = ">50K"
    else:
        income_bracket = "<=50K"

    return {
        "prediction_code": int(prediction),
        "income_prediction": income_bracket
    }