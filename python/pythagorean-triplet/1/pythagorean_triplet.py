def triplets_with_sum(n):
    triplet = []
    for a in range(1, n // 3 + 1):
        for b in range(a + 1, (n - a) // 2 + 1):
            c = n - a - b
            if a * a + b * b == c * c:
                triplet.append([a, b, c])
    return triplet
