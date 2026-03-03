from transformers import pipeline
import numpy as np

classifier = pipeline(
    "image-classification",
    model="google/vit-base-patch16-224"
)

def compute_entropy(scores):
    probs = np.array(scores)
    return -np.sum(probs * np.log(probs + 1e-9))

def annotate_image(image_path):
    results = classifier(image_path)

    label = results[0]["label"]
    confidence = float(results[0]["score"])

    scores = [r["score"] for r in results[:5]]
    entropy = float(compute_entropy(scores))

    extra_info = {
        "top_predictions": results[:5]
    }

    return label, confidence, entropy, extra_info