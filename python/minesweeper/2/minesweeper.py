def annotate(minefield):
    wrong_lenght = not all(len(minefield[0]) == len(mc) for mc in minefield) if minefield else False
    wrong_char = not all(c in " *"for mc in minefield for c in mc)
    
    # when the board receives malformed input
    if wrong_lenght or wrong_char:
        raise ValueError("The board is invalid with current input.")
    
    neightbours = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    result = []
    for r,mine_row in enumerate(minefield):
        build_column = []
        for c,mine_col in enumerate(mine_row):
            if mine_col == "*":
                build_column.append("*")
                continue
            mines_around = 0
            for nb in neightbours:
                try:
                    if not 0 <= r+nb[0] < len(minefield) or not 0 <= c+nb[1] < len(minefield[0]):
                        continue
                    if minefield[r+nb[0]][c+nb[1]] == "*":
                        mines_around += 1
                except IndexError:
                    continue
            build_column.append(str(mines_around) if mines_around else " ")
        result.append("".join(build_column))
        
    return result