def mock_search(symptom):
    database = {
        "fever": "Possible infection",
        "headache": "Could be stress or migraine"
    }

    return database.get(symptom.lower(), "No data")
