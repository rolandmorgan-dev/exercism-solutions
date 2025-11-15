grains = [0]

# How many grains on a given square
def square(number):
    global grains
    if number == 1:
        grains = [1]
        return grains[0]
    elif 1 < number < 65:
        grains = [1]
        for field in range(0, number-1):
            grains.append(grains[field]*2)
        return grains[-1]
    else:
        raise ValueError("square must be between 1 and 64")

# The total number of grains on the chessboard
def total():
    return sum(grains)
