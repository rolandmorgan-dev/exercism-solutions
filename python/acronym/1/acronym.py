import re

# Phrase to acronym function
def abbreviate(words : str) -> str:
    words = re.sub(r"[^\w\s-]|_", "", words)
    return "".join(re.findall(r"\b[A-Za-z]", words)).upper()
