# Calculating the square root of a given number
def square_root(n : int) -> int:
    for i in range(n+1):
        if i * i == n:
            return i