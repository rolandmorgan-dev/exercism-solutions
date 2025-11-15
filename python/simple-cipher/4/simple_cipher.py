from itertools import cycle; import secrets, string

class Cipher:
    def __init__(self, key=None):
        self.key = key or "".join(secrets.choice(string.ascii_letters) for _ in range(100)).lower()

    def encode(self, text):
        return "".join(chr((ord(c) + ord(k) - 2 * 97) % 26 + 97) for c, k in zip(text, cycle(self.key)))

    def decode(self, text):
        return "".join(chr((ord(c) - ord(k) + 26) % 26 + 97) for c, k in zip(text, cycle(self.key)))
