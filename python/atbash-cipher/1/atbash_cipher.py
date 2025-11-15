import re

table = "abcdefghijklmnopqrstuvwxyz"

# Encoding string input
def encode(text : str) -> str:
    # Removing punctuations
    text = re.sub(r'[^\w]', '', text.lower())
    # Remapping strings and translate from mapped strings
    mapped_text = text.maketrans(table, table[::-1])
    missing_spaces = text.translate(mapped_text)
    cipher_text = ""
    # Add a space after every 5 characters
    for i in range(len(missing_spaces)):
        if i != 0 and i % 5 == 0:
            cipher_text += " "
        cipher_text += missing_spaces[i]
    return cipher_text

# Decoding string input
def decode(reveal : str) -> str:
    # Removing spaces
    reveal = reveal.lower().replace(" ", "")
    # Remapping strings and translate from mapped strings
    decoded_text = reveal.maketrans(table[::-1], table)
    return reveal.translate(decoded_text)
