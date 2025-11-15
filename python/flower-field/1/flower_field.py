def annotate(garden: list[str]) -> list[str]:
    row_len = len(garden)
    col_len = len(garden[0]) if garden else 0

    if any(len(row) != col_len or c not in " *" for row in garden for c in row):
        raise ValueError("The board is invalid with current input.")

    directions = ((-1, -1), (-1, 0), (-1, 1),
                  ( 0, -1), 		 ( 0, 1),
                  ( 1, -1), ( 1, 0), ( 1, 1))

    rebuild_garden = []
    for row in range(row_len):
        build_row = []
        for col in range(col_len):
            count = 0
            for dr, dc in directions:
                n_row, n_col = dr + row, dc + col
                if 0 <= n_row < row_len and 0 <= n_col < col_len:
                    count += garden[n_row][n_col] == "*"
            field = garden[row][col]
            build_row.append(field if count == 0 or field == "*" else str(count))

        rebuild_garden.append("".join(build_row))

    return rebuild_garden