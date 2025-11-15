# Prime factors of a given natural number
def factors(num : int) -> list:
    results, divisor = [], 2
    while num != 1:
        if num % divisor == 0:
            num //= divisor
            results.append(divisor)
        else:
            divisor += 1
    return results
