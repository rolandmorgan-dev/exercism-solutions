from string import punctuation as punc

"""
Implementing the classic method for composing secret messages
called square code.
"""
def cipher_text(text : str) -> str:
    # remove punctuations, whitespaces & convert to lowercase
    text = text.translate(str.maketrans('', '', punc + " ")).lower()
    
    if not text: return ""
    
    # square root & ceil rounding
    x = len(text) ** 0.5
    sq_calc = int(x) + (x > int(x))
    
    # equal length chunks of text
    parts = [text[i:i+sq_calc].ljust(sq_calc) for i in range(0, len(text), sq_calc)]
    
    # transpose chunks for cipher text
    zipped = zip(*parts)
    
    # transposed chunks into a single string, seperated by spaces
    return " ".join("".join(c) for c in zipped)