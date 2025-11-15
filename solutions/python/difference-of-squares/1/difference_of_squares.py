# The square of the sum of the first ten natural numbers 
def square_of_sum(number : int) -> int:
    return sum(num for num in range(1,number+1)) ** 2

# The sum of the squares of the first ten natural numbers
def sum_of_squares(number : int) -> int:
    return sum(num ** 2 for num in range(1,number+1))

# The difference between the square of the sum and the sum of the squares
def difference_of_squares(number : int) -> int:
    return square_of_sum(number)-sum_of_squares(number)
