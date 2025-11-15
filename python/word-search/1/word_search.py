class Point:
    def __init__(self, x: int, y: int):
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle: list[str]):
        self.puzzle = puzzle

    def search(self, word: str):
        directions = ((-1,-1), (-1, 0), (-1, 1),
                      ( 0,-1),  		( 0, 1),
                      ( 1,-1), ( 1, 0), ( 1, 1))
        
        rows = len(self.puzzle)
        cols = len(self.puzzle[0]) if self.puzzle else 0

        for row in range(rows):
            for col in range(cols):
                # start cell must match the first character of the word
                if self.puzzle[row][col] != word[0]:
                    continue

                for dr, dc in directions:
                    c_row, c_col = row, col # current row = c_row, current col = c_col
                    for i in range(1, len(word)):
                        c_row += dr
                        c_col += dc
                        if not (0 <= c_row < rows and 0 <= c_col < cols): # bounds check
                            break
                        if self.puzzle[c_row][c_col] != word[i]: # if character differs
                            break
                    else:
                        # word found; return start and end positions
                        return Point(row, col), Point(c_row, c_col)