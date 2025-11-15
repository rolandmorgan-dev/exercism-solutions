# Comparison categories
EQUAL = 1
SUBLIST = 2
SUPERLIST = 3
UNEQUAL = 4

# Function for list comparison
def sublist(a : list, b : list) -> int:
    # Equal : 1
    if a == b:
        return EQUAL

    # Sublist : 2
    if len(a) <= len(b):
        if any(a == b[i:i+len(a)] for i in range(len(b)-len(a)+1)):
            return SUBLIST

    # Superlist : 3
    if len(a) >= len(b):
        if any(b == a[i:i+len(b)] for i in range(len(a)-len(b)+1)):
            return SUPERLIST

    # Unequal : 4
    return UNEQUAL
