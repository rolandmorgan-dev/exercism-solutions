def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    
    if row_count < 2:
        return [[1]] if row_count else []
    
    r = rows(row_count-1)
    
    return r + [[(r[-1][i - 1] if i - 1 >= 0 else 0) +
                 (r[-1][i] if i < len(r[-1]) else 0)
                 for i in range(row_count)]]