# Calculation of Hamming distance between two DNA strands
def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    mistakes = 0
    for index in range(len(strand_a)):
        if strand_a[index] != strand_b[index]:
            mistakes += 1
    return mistakes