def needs_review(confidence, entropy,
                 confidence_threshold=0.75,
                 entropy_threshold=1.0):

    if confidence < confidence_threshold:
        return True

    if entropy > entropy_threshold:
        return True

    return False