# Position of two queens on a chess table
class Queen:
    def __init__(self, row : int, column : int):
        
        # checks for wrong input
        if row < 0: raise ValueError("row not positive")
        if row > 7: raise ValueError("row not on board")
        if column < 0: raise ValueError("column not positive")
        if column > 7: raise ValueError("column not on board")
        
        self.row = row
        self.column = column
        
        # check if a queen can attack the other queen
    def can_attack(self, another_queen) -> bool:
        q2_r, q2_c = another_queen.row, another_queen.column
        
        # error check, ValueError if both queen on the same place
        if self.row == q2_r and self.column == q2_c:
            raise ValueError(
                "Invalid queen position: both queens in the same square")
        
        # check for attack in:
        # \ main diagonal (q1r-q1c == q2r-2c) and (q1r+q1c == q2r+q2c) / anti-diagonal
        if (self.row-self.column) == (q2_r-q2_c) or (self.row+self.column) == (q2_r+q2_c):
            return True
        
        # check for attack in:
        # ━ horizontal (q1r == q2r) and (q1c == q2c) | vertical
        if (self.row == q2_r) or (self.column == q2_c):
            return True
        return False
