from string import ascii_lowercase as letters

def rotate(text, key):
    rotated = ""
    for char in text:
        if char.isalpha():
            for index, letter in enumerate(letters):
                if char == letter:
                    rotated += letters[(index + key) % len(letters)]
                elif char == letter.upper():
                    rotated += letters[(index + key) % len(letters)].upper()
        else:
            rotated += char
    return rotated