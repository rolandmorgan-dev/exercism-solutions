from collections import defaultdict

WHITE = "W"
BLACK = "B"
NONE = " "

STEPS = ((0,1),(0,-1),(1,0),(-1,0))

# Count territories of each player in a Go game
# Args -> Board(list[str]) = A two-dimensional Go board
class Board:
    def __init__(self, board):
        if not board: raise ValueError('Board argument is empty')
        self.board = board
    
    def is_valid_coord(self, x: int, y: int) -> bool:
        return 0 <= x < len(self.board[0]) and 0 <= y < len(self.board)

    def territory(self, x: int, y: int) -> tuple[str, set[tuple[int, int]]]:
        if not self.is_valid_coord(x, y):
            raise ValueError('Invalid coordinate')
        if self.board[y][x] != NONE:
            return (NONE, set())
        
        stones = set()
        territory_coords = set()
        stack = {(x, y)}
        while stack:
            coord = stack.pop()
            x, y = coord
            if coord not in territory_coords:
                if self.board[y][x] == NONE:
                    territory_coords.add(coord)
                    for s in STEPS:
                        if self.is_valid_coord(x + s[0], y + s[1]):
                            stack.add((x + s[0], y + s[1]))
                else:
                    stones.add(self.board[y][x])
            
        return (next(iter(stones)) if len(stones) == 1 else NONE, territory_coords)

    def territories(self) -> dict[str, set[tuple[int, int]]]:
        territory_map = defaultdict(set)
        seen = set()
        
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if (x, y) in seen or self.board[y][x] != NONE:
                    continue
                stone, coordinates = self.territory(x, y)
                territory_map[stone].update(coordinates)
                seen.update(coordinates)
        return territory_map