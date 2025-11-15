# Function to count the rectangles in an ASCII diagram
def rectangles(diagram : str) -> int:
    if not diagram: return 0
    
    # positions of "+" saved
    plus_idx = [(r, c) for r in range(len(diagram)) for c in range(len(diagram[r])) if diagram[r][c] == "+"]
    
    rectangles = 0
    
    # loop through the saved "+" list
    for i in range(len(plus_idx)-1):
        r1, c1 = plus_idx[i]
        for diagonal in range(i+1, len(plus_idx)):
            r2, c2 = plus_idx[diagonal]
            
            # skip those that can't be rectangles
            if r1 == r2 or c1 >= c2: continue
            
            # top side & bottom side check
            top_side = all(diagram[r1][c] in "+-" for c in range(c1, c2 + 1))
            bottom_side = all(diagram[r2][c] in "+-" for c in range(c1, c2 + 1))
            
            # left side & right side check
            left_side = all(diagram[r][c1] in "+|" for r in range(r1, r2 + 1))
            right_side = all(diagram[r][c2] in "+|" for r in range(r1, r2 + 1))
            
            # add 1 if it's a rectangle
            if top_side and bottom_side and left_side and right_side:
                rectangles += 1

    return rectangles