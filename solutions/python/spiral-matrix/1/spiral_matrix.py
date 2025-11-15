def spiral_matrix(size : int) -> list:
    if size <= 0: return []
    
    # creating matrix of the given size
    matrix = [[1] * size for _ in range(size)]
    
    # keeping track of visited grids
    been = {(0,0)}
    # directions in spiral form +correction
    dr = ((0,1),(0,-1),(1,0),(-1,0),(0,-1),(0,1),(-1,0),(1,0))
    
    # number to be placed on a grid
    num = 1
    
    # (dynamic row/col tracking) and (direction steps -> (dr))
    row = col = step = 0
    while num != size * size:
        num += 1
        row += dr[step][0]
        col += dr[step][1]
        try:
            if (row,col) not in been:
                if row < 0 or col < 0: raise IndexError
                matrix[row][col] = num
                been.add((row,col))
            else:
                step = (step+1) % 8
                num -= 1
        except IndexError:
            step = (step+1) % 8
            num -= 1
            continue
    
    return matrix