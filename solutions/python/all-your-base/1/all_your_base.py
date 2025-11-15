def rebase(base, digits, to_base):
    if not base >= 2:
        raise ValueError("input base must be >= 2")
    if not all(0 <= digit < base for digit in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if not to_base >= 2:
        raise ValueError("output base must be >= 2")
    
    # Convert digits from input base to base 10
    base_10 = 0
    for index, number in enumerate(reversed(digits)):
        base_10 += number * (base ** index)
    
    # Convert base 10 to the target base
    result = []
    while base_10:
        result.append(base_10 % to_base)
        base_10 //= to_base
        
    return result[::-1] if result else [0]