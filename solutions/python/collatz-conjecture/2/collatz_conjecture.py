# Collatz Conjecture, counting steps to reach 1
def steps(number: int) -> int:
    steps = 0
    if 0 < number:
        while number != 1:
            number = number * 3 + 1 if number % 2 else number // 2
            steps += 1
    else:
        raise ValueError("Only positive integers are allowed")
    return steps
