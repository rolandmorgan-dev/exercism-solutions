import re

# Phrase to acronym function
def abbreviate(words : str) -> str:
    return "".join((re.findall(r"\b[A-Za-z]", re.sub(r"[^\w\s-]|_", "", words).upper())))
