# The square of the sum of the first ten natural numbers 
def square_of_sum(n : int) -> int:
    return (n * (n + 1) // 2) ** 2

# The sum of the squares of the first ten natural numbers
def sum_of_squares(n : int) -> int:
    return n * (n + 1) * (2 * n + 1) // 6

# The difference between the square of the sum and the sum of the squares
def difference_of_squares(n : int) -> int:
    return square_of_sum(n) - sum_of_squares(n)
