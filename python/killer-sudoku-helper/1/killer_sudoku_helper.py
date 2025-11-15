from itertools import combinations as combos

# Killer Sudoku Helper
def combinations(cage_sum : int, cage_size : int, exclude : int = None) -> list[list]:
    numbers = [1,2,3,4,5,6,7,8,9]
    results = []
    
    for num in exclude:
        if num in numbers:
            numbers.remove(num)
    
    for combo in combos(numbers, cage_size):
        if sum(combo) == cage_sum:
            results.append(list(combo))
    
    return results