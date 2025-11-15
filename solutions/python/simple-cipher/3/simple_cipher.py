class Cipher:
    def __init__(self, key="aaaaaaaaaa"):
        self.key, self.keylen, self.ABC = key, len(key), "abcdefghijklmnopqrstuvwxyz"
        
    def encode(self, text):
        return "".join(self.ABC[(self.ABC.index(char) + self.ABC.index(self.key[i % self.keylen])) % 26] for i, char in enumerate(text))

    def decode(self, text):
        return "".join(self.ABC[(self.ABC.index(char) - self.ABC.index(self.key[i % self.keylen])) % 26] for i, char in enumerate(text))
