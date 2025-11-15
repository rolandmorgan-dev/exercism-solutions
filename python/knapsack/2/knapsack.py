from itertools import combinations

def maximum_value(maximum_weight: int, items: list[dict]) -> int:
    items = tuple((item["weight"], item["value"]) for item in items)
    
    max_value = 0
    for i in range(1, len(items) + 1):
        knapsack = combinations(items, i)
        for combination in knapsack:
            weight = sum(weight for weight,value in combination)
            if weight <= maximum_weight:
                value = sum(value for weight,value in combination)
                if max_value < value: max_value = value
    return max_value