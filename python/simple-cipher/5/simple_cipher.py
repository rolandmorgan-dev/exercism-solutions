from itertools import cycle; from string import ascii_lowercase as alpha; import secrets

class Cipher:
    def __init__(self, key=None):
        self.key = key or "".join(secrets.choice(alpha) for _ in range(secrets.randbelow(14)+37))

    def encode(self, text):
        return "".join(chr((ord(c) + ord(k) - 2 * 97) % 26 + 97) for c, k in zip(text, cycle(self.key)))

    def decode(self, text):
        return "".join(chr((ord(c) - ord(k)) % 26 + 97) for c, k in zip(text, cycle(self.key)))