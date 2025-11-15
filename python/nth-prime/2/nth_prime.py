# Prime check
def is_prime(num : int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Nth prime
def prime(n : int) -> int:
    if n < 1:
        raise ValueError('there is no zeroth prime')
    primes, nth_prime = 0, 2
    while True:
        if is_prime(nth_prime):
            primes += 1
            if primes == n:
                return nth_prime
        nth_prime += 1