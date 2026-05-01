def risk_agent(data_text):
    data_text = data_text.lower()

    if "chest pain" in data_text:
        return "high"
    if "difficulty breathing" in data_text:
        return "high"

    return "low"
