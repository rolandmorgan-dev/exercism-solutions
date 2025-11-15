abc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

class Cipher:
    def __init__(self, key="aaaaaaaaaa"):
        self.key = key
        self.keylen = len(self.key)
        
    def encode(self, text):
        encoded = []
        for i, char in enumerate(text):
            index1 = abc.find(char)
            index2 = abc.find(self.key[i % self.keylen])
            encoded.append(abc[index1+index2])
            
        return "".join(encoded)

    def decode(self, text):
        decoded = []
        for i, char in enumerate(text):
            index1 = abc.find(char)
            index2 = abc.find(self.key[i % self.keylen])
            decoded.append(abc[index1-index2])
            
        return "".join(decoded)
