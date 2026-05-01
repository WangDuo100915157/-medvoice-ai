from fastapi import FastAPI
from pydantic import BaseModel
from app.orchestrator import run_pipeline

app = FastAPI(
    title="MedVoice AI API",
    description="Medical voice/text agent demo with structured extraction, tool insights, risk detection, and summary generation.",
    version="1.0.0"
)

class AnalyzeRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "message": "MedVoice AI API is running",
        "docs": "Go to /docs to test the API"
    }

@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    result = run_pipeline(request.text)
    return result
