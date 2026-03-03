import requests
import os

HF_API_TOKEN = os.getenv("HF_API_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/typeform/distilbert-base-uncased-mnli"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

def query_model(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()