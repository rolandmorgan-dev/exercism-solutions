# Function to output all the contiguous substrings of length
def slices(series : str, length : int):
    # error check
    if length == 0: raise ValueError("slice length cannot be zero")
    if length < 0 : raise ValueError("slice length cannot be negative")
    if not series : raise ValueError("series cannot be empty")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    
    # append given length of slices
    result = []
    for i in range(len(series)):
        if len(series[i:i+length]) == length:
            result.append(series[i:i+length])
    return result
