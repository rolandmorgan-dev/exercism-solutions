# Prime factors of a given natural number
def factors(num : int) -> list:
    results, divisor, factor = [], 2, num
    while factor != 1:
        if factor % divisor == 0:
            factor = factor // divisor
            results.append(divisor)
        else:
            divisor += 1
    return results
