def rails(l_txt, r):
    return sorted((r - abs(i % (2 * r) - r), i) for i in range(l_txt))

def encode(m, r):
    return ''.join(m[i] for _, i in rails(len(m), r-1))

def decode(m, r):
    n = iter(i for _, i in rails(len(m), r-1))
    return ''.join(c for _, c in sorted((next(n), m[i]) for i in range(len(m))))