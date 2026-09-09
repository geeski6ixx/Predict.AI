from fastapi import FastAPI
from prediction import predict_match

app = FastAPI(title="PredictAI API")


@app.get("/")
def home():
    return {
        "message": "PredictAI API is running!",
        "status": "success"
   }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/predict")
def predict(home_team: str, away_team: str):
    return predict_match(home_team, away_team)