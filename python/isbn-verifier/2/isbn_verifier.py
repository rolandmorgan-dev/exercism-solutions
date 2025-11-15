def is_valid(isbn):
    isbn = list(isbn.replace("-",""))
    if len(isbn)!=10: return False
    if isbn[-1] == "X": isbn[-1] = "10"
    if not all(char.isdigit() for char in isbn): return False
    return sum(int(x)*y for x,y in zip(isbn[::-1], range(1, 11))) % 11 == 0