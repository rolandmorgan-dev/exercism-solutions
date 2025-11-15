def reverse(text):
    if not text:
        return text
    return reverse(text[1:]) + text[0]