# Triangle validity check based on the Triangle Inequality Theorem
def is_valid_triangle(sides: list) -> bool:
    sides.sort()
    return sides[0] + sides[1] > sides[2]

# Equilateral check
def equilateral(sides: list) -> bool:
    if any(n <= 0 for n in sides) or not is_valid_triangle(sides): return False
    return len(set(sides)) == 1

# Isosceles check
def isosceles(sides: list) -> bool:
    if any(n <= 0 for n in sides) or not is_valid_triangle(sides): return False
    return len(set(sides)) <= 2

# Scalene check
def scalene(sides: list) -> bool:
    if any(n <= 0 for n in sides) or not is_valid_triangle(sides): return False
    return len(set(sides)) == 3