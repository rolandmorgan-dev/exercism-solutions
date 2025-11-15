def steps(number):
    if 0 < number:
        steps_taken = 0
        while number != 1:
            steps_taken += 1
            if number % 2 == 0:
                number //= 2
            elif number % 2 == 1:
                number = number * 3 + 1
        return steps_taken
    else:
        raise ValueError("Only positive integers are allowed")