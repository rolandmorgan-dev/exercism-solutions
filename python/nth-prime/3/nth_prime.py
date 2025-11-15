# Prime check
def is_prime(num : int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True

# Nth prime
def prime(n : int) -> int:
    if n == 0: raise ValueError('there is no zeroth prime')
    if n <  0: raise ValueError('negative input is not valid')
    primes, num_check = 0, 2
    while True:
        if is_prime(num_check):
            primes += 1
            if primes == n:
                return num_check
        num_check += 1
