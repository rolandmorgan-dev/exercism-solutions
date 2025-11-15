# Killer Sudoku Helper
def combinations(cage_sum : int, cage_size : int, exclude : list = []) -> list[list]:
    numbers = [n for n in range(1, 10) if n not in exclude]
    n_len = len(numbers)
    
    if cage_size > n_len:
        raise ValueError("The cage would contain a duplicate digit.")
    
    indices = list(range(cage_size))
    
    results = []
    while True:
        if sum(numbers[i] for i in indices) == cage_sum:
            results.append([numbers[i] for i in indices])
        
        for i in reversed(range(cage_size)):
            if indices[i] != i + n_len - cage_size: break
        else: return results
        
        indices[i] += 1
        
        for j in range(i + 1, cage_size):
            indices[j] = indices[j - 1] + 1