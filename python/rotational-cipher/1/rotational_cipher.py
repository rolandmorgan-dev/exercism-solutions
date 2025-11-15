from string import ascii_lowercase

def rotate(text, key):
    chars, letters = list(text), list(ascii_lowercase)
    rotated = ""
    for char in chars:
        if char.isalpha():
            for index, letter in enumerate(letters):
                if char == letter:
                    rotated += letters[(index + key) % len(letters)]
                elif char == letter.upper():
                    rotated += letters[(index + key) % len(letters)].upper()
        else:
            rotated += char
    return rotated