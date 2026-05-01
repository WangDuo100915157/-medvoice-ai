import requests

def summary_agent(data, risk):
    prompt = f"""
Given the structured patient data:
{data}

Risk level:
{risk}

Write a short clinical-style summary.
"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt, "stream": False}
    )

    return response.json()["response"]
