from itertools import combinations

def maximum_value(maximum_weight: int, items: list[dict]) -> int:
    items = [(item["weight"], item["value"]) for item in items]
    
    max_value = 0
    for i in range(1, len(items) + 1):
        knapsack = set(combinations(items, i))
        for combination in knapsack:
            weight = sum(a for a,b in combination)
            if weight <= maximum_weight:
                value = sum(b for a,b in combination)
                max_value = value if max_value < value else max_value
    return max_value