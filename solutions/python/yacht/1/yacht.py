from collections import Counter

ONES, TWOS, THREES, FOURS, FIVES, SIXES = 1, 2, 3, 4, 5, 6
LITTLE_STRAIGHT, BIG_STRAIGHT, FOUR_OF_A_KIND = "LITTLE", "BIG", "FOUR"
CHOICE, FULL_HOUSE, YACHT = "CHOICE", "FULL", "YACHT"

# Function for the game of Yacht
def score(dice, Set):
    Count = Counter(dice)
    
    if Set == "CHOICE":
        return sum(dice)
    
    elif Set == "FULL":
        if len(Count.values()) == 2 and 4 not in Count.values():
            return sum(dice)
    
    elif Set == "YACHT":
        if len(set(dice)) == 1:
            return 50
    
    elif Set == "LITTLE":
        if [1,2,3,4,5] == sorted(dice):
            return 30
    
    elif Set == "BIG":
        if [2,3,4,5,6] == sorted(dice):
            return 30
    
    elif Set == "FOUR":
        return next((key*4 for key, value in Count.items() if value >= 4), 0)
    
    # ones to sixes
    else: return Set * Count.get(Set, 0)
    return 0
