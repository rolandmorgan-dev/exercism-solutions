from string import ascii_lowercase as asci_low, punctuation as punc
cypher_map = str.maketrans(asci_low, asci_low[::-1], punc + " ")

def encode(text : str) -> str:
    return " ".join(text.lower().translate(cypher_map)[i:i+5] for i in range(0, len(text), 5)).strip()

def decode(text : str) -> str:
    return text.translate(cypher_map)
