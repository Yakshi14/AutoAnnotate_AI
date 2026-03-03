import json
import fitz


def parse_file(uploaded_file):
    filename = uploaded_file.name.lower()

    if filename.endswith(".json"):
        raw_data = json.load(uploaded_file)

        # Case 1: list of strings
        if isinstance(raw_data, list) and isinstance(raw_data[0], str):
            return [{"id": i, "text": text} for i, text in enumerate(raw_data)]

        # Case 2: list of dicts with "text" key
        if isinstance(raw_data, list) and isinstance(raw_data[0], dict):
            if "text" in raw_data[0]:
                return raw_data

        # Case 3: dictionary
        if isinstance(raw_data, dict):
            return [{"id": 0, "text": str(raw_data)}]

        return []

    elif filename.endswith(".txt"):
        text = uploaded_file.read().decode("utf-8")
        lines = [l.strip() for l in text.split("\n") if l.strip()]
        return [{"id": i, "text": line} for i, line in enumerate(lines)]

    elif filename.endswith(".pdf"):
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in pdf:
            text += page.get_text()

        lines = [l.strip() for l in text.split("\n") if l.strip()]
        return [{"id": i, "text": line} for i, line in enumerate(lines)]

    return []