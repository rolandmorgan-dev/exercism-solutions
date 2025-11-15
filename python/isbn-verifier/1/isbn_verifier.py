from string import ascii_letters as letters

def is_valid(isbn):
    isbn = isbn.replace("-","")
    if len(isbn) != 10 or isbn[-1] in letters.replace("X",""):
        return False
    for letter in letters:
        if letter in isbn[:-1]:
            return False

    last = 10 if isbn[-1] == "X" else int(isbn[-1])
    counter = 10
    summ = 0
    for i in isbn[:-1]:
        if counter > 1:
            result = int(i) * counter
            summ += result
        counter -= 1
    return (summ + last) % 11 == 0