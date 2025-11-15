from string import ascii_lowercase as letters
from math import gcd


def encode(plain_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")
    
    encoded = []
    for char in plain_text.lower():
        if char_is_letter:= char in letters:
            shift = (a * letters.index(char) + b) % 26
        if char_is_letter or char.isdigit():
            encoded.append(letters[shift] if char_is_letter else char)
    return " ".join("".join(encoded[i:i+5]) for i in range(0, len(encoded), 5))


def decode(ciphered_text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a and m must be coprime.")

    decoded = []
    for char in ciphered_text.lower():
        if char_is_letter:= char in letters:
            shift = pow(a, -1, 26) * (letters.index(char) - b) % 26
        if char_is_letter or char.isdigit():
            decoded.append(letters[shift] if char_is_letter else char)
    return "".join(char for char in decoded)