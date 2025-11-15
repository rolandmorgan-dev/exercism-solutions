"""
Simple bowling game scorer and validator.
Supports standard 10-frame bowling rules including bonus rolls.
"""
class BowlingGame:
    def __init__(self):
        self.frame = 1
        self.frame_scores = {i: [] for i in range(1, 11)}

    # Records a roll and handles frame progression and validation.
    def roll(self, pins: int):
        current_scores = self.frame_scores[self.frame]
        self.roll_validate(pins, current_scores)

        self.frame_scores[self.frame].append(pins)

        if self.frame < 10:
            if len(current_scores) == 2 or current_scores[0] == 10:
                self.frame += 1

    # Calculates the total game score.
    def score(self):
        last = self.frame_scores[10]
        if len(last) < 2 or (len(last) == 2 and (last[0] == 10 or sum(last[:2]) == 10)):
            scores = self.frame_scores[self.frame]
            raise IndexError(f"incomplete game, frame: {self.frame} scores: {scores}")
        rolls = [scores for frame in self.frame_scores.values() for scores in frame]
        max_index = len(rolls)
        score = i = 0
        for _ in range(9):
            # strike
            if rolls[i] == 10:
                score += sum(rolls[i:i+3])
                i += 1
            # spare
            elif rolls[i] + rolls[i+1] == 10:
                score += sum(rolls[i:i+3])
                i += 2
            # open Frame
            else:
                score += sum(rolls[i:i+2])
                i += 2
        score += sum(rolls[i:max_index])
        return score

    # Validates roll input and enforces rules for a roll.
    def roll_validate(self, pins: int, scr: list):
        if not (0 <= pins <= 10):
            raise ValueError("invalid score, valid score range is: 0-10")

        if (len(scr) == 1 and scr[0] != 10 and scr[0] + pins > 10 or
            len(scr) == 2 and scr[0] == 10 and scr[1] != 10 and scr[1]+pins > 10):
            raise ValueError("invalid bonus roll, pins exceed allowed max")
        
        if self.frame < 10: return
        
        if len(scr) == 2 and scr[0] != 10 and sum(scr) < 10:
            raise IndexError("no bonus roll after an open tenth frame")

        if len(scr) == 3:
            raise IndexError("game has ended, no more rolls left")