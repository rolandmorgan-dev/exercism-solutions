from string import ascii_lowercase

def is_pangram(sentence):
    for eng_alphabet in ascii_lowercase:
        if eng_alphabet not in sentence.lower():
            return False
    return True
