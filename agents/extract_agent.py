def extract_agent(text):
    text = text.lower()

    symptoms = []
    duration = ""
    medication = ""

    if "fever" in text:
        symptoms.append("fever")
    if "headache" in text:
        symptoms.append("headache")

    if "3 days" in text:
        duration = "3 days"

    return {
        "symptoms": symptoms,
        "duration": duration,
        "medication": medication
    }
