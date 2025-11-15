from itertools import count, islice

def isprime(n): return all(n % i > 0 for i in range(2, int(n ** 0.5) + 1))

def prime(num):
    if num == 0: raise ValueError("there is no zeroth prime")
    primes = islice(filter(isprime, count(2)), num)
    return next(islice(primes, num - 1, num))