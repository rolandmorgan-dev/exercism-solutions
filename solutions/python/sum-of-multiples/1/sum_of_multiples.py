"""
Function that calculates the energy points that get awarded to players when they complete a level
"""
def sum_of_multiples(level : int, magical_items : list) -> int:
    energy = []
    for item in magical_items:
        for num in range(1,level):
            if item != 0 and num % item == 0:
                energy.append(num)
    return sum(set(energy)) if energy else 0