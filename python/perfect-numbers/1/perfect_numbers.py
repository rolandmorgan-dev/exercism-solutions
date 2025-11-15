def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    summ = 0
    for num in range(1,number):
        if number % num == 0:
            summ += num
    if summ == number: return "perfect"
    if summ > number: return "abundant"
    return "deficient"
