# How many grains on a given square
def square(number):
    if 1 <= number <= 64:
        return 2 ** (number-1)
    else:
        raise ValueError("square must be between 1 and 64")

# The total number of grains on a chessboard of 64 fields
def total():
    return 2 ** 64 -1
