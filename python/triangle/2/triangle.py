# Triangle validity check (decorator)
def is_valid_triangle(triangle_func):
    def check(sides):
        a,b,c = sorted(sides)
        return triangle_func(sides) and 0 < a and a + b > c
    return check

# Equilateral check
@is_valid_triangle
def equilateral(sides: list) -> bool:
    return len(set(sides)) == 1

# Isosceles check
@is_valid_triangle
def isosceles(sides: list) -> bool:
    return len(set(sides)) <= 2

# Scalene check
@is_valid_triangle
def scalene(sides: list) -> bool:
    return len(set(sides)) == 3