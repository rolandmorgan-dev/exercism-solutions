# Prime check
def is_prime(num: int) -> bool:
    return all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

# Nth prime
def prime(nth : int) -> int:
    if nth == 0: raise ValueError('there is no zeroth prime')
    primes, number = 0, 2
    while True:
        primes += is_prime(number)
        if primes == nth: return number
        number += 1
