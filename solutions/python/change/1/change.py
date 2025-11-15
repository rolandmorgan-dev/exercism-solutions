from itertools import combinations_with_replacement as x

def find_fewest_coins(a, b):
    try: return list(next(c for i in range(b // a[0] + 1) for c in x(a, i) if sum(c) == b))
    except StopIteration: raise ValueError("target can't be negative" if b < 0 else "can't make target with given coins")