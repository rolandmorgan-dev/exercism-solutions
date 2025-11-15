# Calculation of Hamming distance between two DNA strands
def distance(a: str, b: str) -> int:
    if len(a)!=len(b):raise ValueError("Strands must be of equal length.")
    return sum(str1!=str2 for str1, str2 in zip(a, b))