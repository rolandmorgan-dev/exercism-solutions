from functools import lru_cache
from collections import Counter
from itertools import combinations

# Discounts based on group size
DISCOUNTS = (1.00, 0.95, 0.90, 0.80, 0.75)

def total(basket):
    # Count books and convert to tuple for hashing
    counts = tuple(Counter(basket).values())
    return _min_price(counts)

@lru_cache(maxsize=None)
def _min_price(counts):
    if not any(counts):  # Base case: no books left
        return 0

    min_total = float('inf')

    # Get indices of books we still have copies of
    books_with_copies = [i for i, c in enumerate(counts) if c > 0]

    # Try all group sizes from 1 to 5
    for group_size in range(1, 6):
        for group in combinations(books_with_copies, group_size):
            # Create new counts after using 1 copy from each in group
            new_counts = list(counts)
            for idx in group:
                new_counts[idx] -= 1
            # Remove zeros and sort to normalize the state
            new_counts = tuple(sorted([c for c in new_counts if c > 0], reverse=True))

            group_price = group_size * 800 * DISCOUNTS[group_size - 1]
            total_price = group_price + _min_price(new_counts)

            min_total = min(min_total, total_price)

    return int(min_total)