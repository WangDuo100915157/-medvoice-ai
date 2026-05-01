def summary_agent(data, risk):
    symptoms = ", ".join(data.get("symptoms", []))
    duration = data.get("duration", "")

    return f"Patient presents with {symptoms} for {duration}. Risk level is {risk}."
