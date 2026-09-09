from fastapi import FastAPI

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