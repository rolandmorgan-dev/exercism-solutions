class ConnectGame:
    def __init__(self, board):
        self.board = board.replace(" ", "").split("\n")
        self.neighbours = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]

    def get_winner(self):
        return next((player for player in ["O", "X"] if self.check(player)), "")

    def check(self, player):
        array = self.board if player == "O" else list(zip(*self.board))
        
        stones = [(0, index) for index, stone in enumerate(array[0]) if stone == player]
        ends = [(len(array) - 1, index) for index, stone in enumerate(array[-1]) if stone == player]
        for stone in stones:
            for neighbour in self.neighbours:
                row = stone[0] + neighbour[0]
                col = stone[1] + neighbour[1]
                if row >= 0 and col >= 0:
                    try:
                        if array[row][col] == player and (row, col) not in stones:
                            stones.append((row, col))
                    except IndexError:
                        continue
        return any(end in stones for end in ends)
