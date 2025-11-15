def rebase(base:int, digits:list, to_base:int) -> list:
    if not base >= 2:
        raise ValueError("input base must be >= 2")
    if not to_base >= 2:
        raise ValueError("output base must be >= 2")
    if not all(0 <= digit < base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    
    # Convert digits from input base to base 10
    decimal = sum(n*base**i for i,n in enumerate(digits[::-1]))
    
    # Convert base 10 to the target base
    result = []
    while decimal:
        result.append(decimal % to_base)
        decimal //= to_base
    
    return result[::-1] if result else [0]
