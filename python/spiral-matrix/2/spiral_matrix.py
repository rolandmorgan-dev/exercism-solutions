def spiral_matrix(size : int) -> list:
    matrix = [[None] * size for _ in range(size)]
    
    dr = ((0,1),(1,0),(0,-1),(-1,0))
    
    y = x = step = 0
    for num in range(size * size):
        matrix[y][x] = num + 1
        
        if (not 0 <= y + dr[step][0] < size or
            not 0 <= x + dr[step][1] < size or
            matrix[y + dr[step][0]][x + dr[step][1]] is not None):
            step = (step+1) % 4
            
        y += dr[step][0]
        x += dr[step][1]
    
    return matrix