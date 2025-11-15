def annotate(minefield : list[str]) -> list[str]:
    # r_c = row lenght, column lenght
    r_c = (len(minefield), len(minefield[0]) if minefield else 0)
    
    wrong_lenght = any(len(m_col) != r_c[1] for m_col in minefield)
    wrong_char = any(char not in " *" for m_row in minefield for char in m_row)
    
    # when the board receives malformed input
    if wrong_lenght or wrong_char:
        raise ValueError("The board is invalid with current input.")
    
    neightbours = ((-1, -1),(-1, 0),(-1, 1),
                   ( 0, -1),		( 0, 1),
                   ( 1, -1),( 1, 0),( 1, 1))
    
    result = []
    for r,mine_row in enumerate(minefield):
        build_column = []
        for c,mine_col in enumerate(mine_row):
            if mine_col == "*":
                build_column.append("*")
                continue
            mines_around = 0
            for nb in neightbours:
                if 0 <= r+nb[0] < r_c[0] and 0 <= c+nb[1] < r_c[1]:
                    if minefield[r+nb[0]][c+nb[1]] == "*":
                        mines_around += 1
            
            build_column.append(str(mines_around) if mines_around else " ")
        result.append("".join(build_column))
        
    return result