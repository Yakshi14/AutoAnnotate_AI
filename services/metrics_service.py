def compute_metrics(records):
    total = len(records)
    auto = len([r for r in records if not r.needs_review])
    review = len([r for r in records if r.needs_review])

    # Example cost model
    cost_per_manual = 0.10
    savings = auto * cost_per_manual

    return total, auto, review, savings