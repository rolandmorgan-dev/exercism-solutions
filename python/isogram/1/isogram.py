from string import ascii_lowercase

def is_isogram(string):
    strings = ""
    for char in string.lower():
        if char in ascii_lowercase:
            if char in strings:
                return False
            strings += char
    return True
