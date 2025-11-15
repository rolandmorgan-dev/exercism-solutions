def largest_product(series : str, size : int) -> int:
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    
    if size < 0:
        raise ValueError("span must not be negative")
    
    if not series.isdigit():
        raise ValueError("digits input must only contain digits")
    
    top = 0
    for i in range(len(series) + 1 - size):
        total = 1
        for j in range(size):
            total *= int(series[i + j])
        top = max(total, top)
    return top