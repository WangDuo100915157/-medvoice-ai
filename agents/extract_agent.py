import json
import requests

def extract_agent(text):
    prompt = f"""
Extract structured clinical information from the input.

Input:
{text}

Return ONLY valid JSON:
{{
  "symptoms": [],
  "duration": "",
  "medication": ""
}}
"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    result = response.json()["response"]

    try:
        return json.loads(result)
    except Exception:
        return {"symptoms": [], "duration": "", "medication": "", "raw_output": result}
