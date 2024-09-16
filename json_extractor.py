import re


def extract_json(text):
    # Use regular expression to extract the JSON part
    json_match = re.search(r'\{.*\}', text, re.DOTALL)
    if json_match:
        return json_match.group(0)
    else:
        return None
