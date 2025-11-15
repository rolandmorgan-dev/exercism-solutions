def annotate(minefield : list[str]) -> list[str]:
    height = len(minefield)
    width = len(minefield[0]) if minefield else 0
    
    wrong_length = any(len(row) != width for row in minefield)
    wrong_char = any(char not in " *" for row in minefield for char in row)
    
    # when the board receives malformed input
    if wrong_length or wrong_char:
        raise ValueError("The board is invalid with current input.")
    
    neighbours = ((-1, -1),(-1, 0),(-1, 1),
                   ( 0, -1),		( 0, 1),
                   ( 1, -1),( 1, 0),( 1, 1))
    
    result = []
    for y, row in enumerate(minefield):
        build_row = []
        
        for x, cell in enumerate(row):
            if cell == "*":
                build_row.append("*")
                continue
            
            mines_around = 0
            for dy, dx in neighbours:
                if 0 <= y + dy < height and 0 <= x + dx < width:
                    if minefield[y + dy][x + dx] == "*":
                        mines_around += 1
            
            build_row.append(str(mines_around) if mines_around else " ")
        
        result.append("".join(build_row))
        
    return result