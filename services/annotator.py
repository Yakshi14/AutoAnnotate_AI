import math
from services.hf_api import query_model

def calculate_entropy(scores):
    entropy = 0
    for s in scores:
        if s > 0:
            entropy -= s * math.log(s)
    return entropy

def annotate_batch(data, labels):

    annotated = []

    for idx, item in enumerate(data[:5]):  # limit for testing

        # Handle different input formats
        if isinstance(item, dict) and "text" in item:
            text = str(item["text"])
        else:
            text = str(item)

        result = query_model(text, labels)

        # NEW HF FORMAT: list of {label, score}
        if not isinstance(result, list) or len(result) == 0:
            continue

        # Extract labels and scores
        labels_list = [r["label"] for r in result]
        scores_list = [r["score"] for r in result]

        top_label = labels_list[0]
        top_score = scores_list[0]

        entropy = calculate_entropy(scores_list)

        annotated.append({
            "id": idx,
            "text": text,
            "label": top_label,
            "confidence": top_score,
            "entropy": entropy
        })

    return annotated