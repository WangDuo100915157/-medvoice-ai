from app.orchestrator import run_pipeline

if __name__ == "__main__":
    text = "Patient has fever for 3 days and headache"

    result = run_pipeline(text)

    print("\n=== RESULT ===")
    print(result)
