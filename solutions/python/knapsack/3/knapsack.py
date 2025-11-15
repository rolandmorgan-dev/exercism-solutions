# Knapsack solution using a Dynamic Programming strategy (avoiding brute-force)
def maximum_value(maximum_weight: int, items: list[dict]) -> int:
    dp = [0] * (maximum_weight + 1)

    for item in items:
        weight, value = item["weight"], item["value"]
        for w in range(maximum_weight, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return max(dp)