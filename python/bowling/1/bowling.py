class BowlingGame:
    def __init__(self):
        self.rolls = []
        self.frame = 1
        self.roll_scores = {1:[], 2:[], 3:[], 4:[], 5:[],
                            6:[], 7:[], 8:[], 9:[], 10:[]}

    # Records a roll and handles frame progression and validation.
    def roll(self, pins : int):
        curr_rolls = self.roll_scores[self.frame]
        self.roll_validate(pins, curr_rolls)
        
        self.roll_scores[self.frame].append(pins)
        self.rolls.append(pins)
        
        if self.frame < 10:
            if len(curr_rolls) == 2 or curr_rolls[0] == 10:
                self.frame += 1

    # Calculates the total game score.
    def score(self):
        last = self.roll_scores[10]
        if len(last) < 2 or (len(last) == 2 and (last[0] == 10 or sum(last[:2]) == 10)):
            raise IndexError(f"incomplete game, 10th frame: {self.roll_scores[10]}")
        score = i = 0
        frame = 1
        max_i = len(self.rolls)
        while i < max_i and frame < 10:
            # strike
            if self.rolls[i] == 10:
                score += sum(self.rolls[i:i+3])
                i += 1
            # spare
            elif self.rolls[i] + self.rolls[i+1] == 10:
                score += sum(self.rolls[i:i+3])
                i += 2
            # open Frame
            else:
                score += sum(self.rolls[i:i+2])
                i += 2
            frame += 1
        score += sum(self.rolls[i:max_i])
        return score
    
    # validates roll input and enforces 10th frame rules for a roll
    def roll_validate(self, pins : int, rolls : list):
        if not (0 <= pins <= 10):
            raise ValueError("invalid score, valid score range is: 0-10")
        
        if len(rolls) == 2 and rolls[0] != 10 and sum(rolls) < 10:
            raise IndexError("cannot throw bonus with an open tenth frame")
        
        if (len(rolls) == 1 and rolls[0] != 10 and rolls[0] + pins > 10 or
            len(rolls) == 2 and rolls[0] == 10 and rolls[1] != 10 and rolls[1]+pins > 10):
            raise ValueError("invalid fill balls")
        
        if self.frame == 10 and len(rolls) == 3:
            raise ValueError("cannot roll after bonus roll")