import requests
import time

HF_API_TOKEN = "YOUR_HF_API_TOKEN"

API_URL = "https://router.huggingface.co/hf-inference/models/typeform/distilbert-base-uncased-mnli"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

def query_model(text, labels):
    payload = {
        "inputs": text[:1000],
        "parameters": {
            "candidate_labels": labels
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()

    print("HF RAW RESPONSE:", data)

    # Handle loading
    if "error" in data and "loading" in data["error"].lower():
        time.sleep(5)
        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()

    return data
