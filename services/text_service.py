from transformers import pipeline
import numpy as np

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

LABELS = ["Finance", "Healthcare", "Technology", "Sports", "Politics", "Other"]

def compute_entropy(scores):
    probs = np.array(scores)
    return -np.sum(probs * np.log(probs + 1e-9))

def annotate_text(text):
    result = classifier(text[:1000], LABELS)

    label = result["labels"][0]
    confidence = float(result["scores"][0])
    entropy = float(compute_entropy(result["scores"]))

    return label, confidence, entropy