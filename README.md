# MedVoice AI

AI-powered medical voice agent system.

## Features

- Extract structured medical data (symptoms, duration)
- Tool-based insights (mock medical knowledge)
- Risk detection
- Clinical summary generation
- FastAPI backend

## API

POST /analyze

Example:

{
  "text": "Patient has fever for 3 days and headache"
}

## Output

{
  "symptoms": ["fever", "headache"],
  "risk": "low",
  "summary": "..."
}

## Run

uvicorn api.server:app --reload

## Demo

### API Overview
![Overview](./截屏2026-05-01 下午4.20.45.png)

### Input Example
![Input](./截屏2026-05-01 下午4.22.28.png)

### Output Result
![Output](./截屏2026-05-01 下午4.22.45.png)
