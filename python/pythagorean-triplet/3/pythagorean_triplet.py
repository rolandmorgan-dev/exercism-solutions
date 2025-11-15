def triplets_with_sum(n : int) -> list:
    
    triplets = []
    for c in range(int(n / 2) - 1, int(0.414 * n), -1):
        d = c * c - n * n + 2 * n * c
        sqrt_d = d ** 0.5 if d >= 0 else None
        
        if sqrt_d is not None and sqrt_d == int(sqrt_d):
            a, b = int((n - c - sqrt_d) / 2), int((n - c + sqrt_d) / 2)
            triplets.append([a, b, c])
            
    return triplets