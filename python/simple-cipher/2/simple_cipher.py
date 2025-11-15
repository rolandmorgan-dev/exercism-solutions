ABC = "abcdefghijklmnopqrstuvwxyz"

class Cipher:
    def __init__(self, key="aaaaaaaaaa"):
        self.key = key
        self.keylen = len(self.key)
        
    def encode(self, text):
        return "".join(
            ABC[(ABC.index(char) + ABC.index(self.key[i % self.keylen])) % 26]
            for i, char in enumerate(text))

    def decode(self, text):
        return "".join(
            ABC[(ABC.index(char) - ABC.index(self.key[i % self.keylen])) % 26]
            for i, char in enumerate(text))