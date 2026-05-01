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

### 1. API Overview
![Overview](./demo-1.png)

### 2. Input Example
![Input](./demo-2.png)

### 3. Output Result (Mock Version)
![Output](./demo-3.png)

### 4. Output Result (LLM Version)
![Output-LLM](./demo-4.png)
