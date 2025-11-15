def triplets_with_sum(n : int) -> list:
    triplets = []
    for c in range(int(n / 2) - 1, int(0.414 * n), -1):
        sqrt = c * c - n * n + 2 * n * c
        d = sqrt ** 0.5 if sqrt >= 0 else None
        if d is not None and d == int(d):
            triplets.append([int((n-c-d)/2), int((n-c+d)/2), c])
    return triplets