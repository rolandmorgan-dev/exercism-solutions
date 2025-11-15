def largest(min_factor, max_factor):
    return palindrome(min_factor, max_factor, 0)


def smallest(min_factor, max_factor):
    return palindrome(min_factor, max_factor, 1)


def palindrome(min_f, max_f, asc):
    if min_f > max_f: raise ValueError("min must be <= max")
    
    range_a = lambda: range(*((min_f,max_f+1) if asc else (max_f,min_f-1,-1)))
    range_b = lambda a: range(*((min_f,a+1) if asc else (a,min_f-1,-1)))
    is_better = lambda a,b,c: a*b > min(c) if asc else a*b < max(c)
    
    palindromes = set()
    for a in range_a():
        for b in range_b(a):
            if palindromes and is_better(a,b,palindromes): break
            if str(a*b) == str(a*b)[::-1]: palindromes.add(a*b)
    
    if not palindromes: return None, []
    
    pal = min(palindromes) if asc else max(palindromes)
    
    # Find all factor pairs of the palindrome within the given bounds
    return pal, [[n, pal // n] for n in range(min_f, max_f+1)
                  if pal % n == 0 and min_f <= pal // n <= max_f]