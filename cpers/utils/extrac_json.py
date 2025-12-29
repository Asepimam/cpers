import re, json

def extract_json(text: str) -> dict:
    match = re.search(r"\{.*\}", text, re.S)
    if not match:
        raise ValueError("No JSON found in model output")
    return json.loads(match.group())
