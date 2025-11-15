def primes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for n in range(2, int(limit**0.5) + 1):
        if sieve[n]:
            for multiple in range(n * n, limit + 1, n):
                sieve[multiple] = False
                
    return [num for num, is_prime in enumerate(sieve) if is_prime]