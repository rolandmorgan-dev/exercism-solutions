class ConnectGame:
    def __init__(self, board):
        self.board = board.replace(' ', '').splitlines()  # Generate 2d array
        self.neighbours = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]  # hex neighbours relative pos in array

    def get_winner(self):  # check player 0, then X, if neither win output ' '
        for player in ['O', 'X']:
            result = self.checker(player)
            if result is True:
                return player
        return ''

    def checker(self, player):
        if player == 'O':  # set parameters for player O
            array = self.board
        if player == 'X':  # set parameters for player X
            array = list(zip(*self.board))  # transpose the board, so X becomes top to down
        # get player first and last row stones
        stones = [(index, 0) for index, stone in enumerate(array[0]) if stone == player]
        ends = [(index, len(array) - 1) for index, stone in enumerate(array[-1]) if stone == player]
        for stone in stones:  # search for stones connected to first row stones, loop till exhaustion
            for neighbour in self.neighbours:
                row = stone[1] + neighbour[1]
                col = stone[0] + neighbour[0]
                if row >= 0 and col >= 0:
                    try:
                        if array[row][col] == player and (col, row) not in stones:
                            stones.append((col, row))  # append stone to end of list so it will be looped over
                    except IndexError:
                        continue
        for end in ends:  # return true if one of the end stones is connected to first row stones
            if end in stones:
                return True