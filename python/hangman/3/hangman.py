# Game status categories
STATUS_ONGOING = "ongoing"
STATUS_WIN = "win"
STATUS_LOSE = "lose"

class Hangman:
    def __init__(self, word):
        self.word = word
        self.guesses = set()
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
    
    def guess(self, letter):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        
        if not letter in self.word or letter in self.guesses:
            self.remaining_guesses -= 1
        self.guesses.add(letter)
        
        if all(char in self.guesses for char in set(self.word)):
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE
    
    def get_masked_word(self):
        return "".join(c if c in self.guesses else "_" for c in self.word)
    
    def get_status(self):
        return self.status