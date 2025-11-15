# Game status categories
STATUS_ONGOING = "ongoing"
STATUS_WIN = "win"
STATUS_LOSE = "lose"

class Hangman:
    def __init__(self, word):
        self.word = word.lower()
        self.guesses = set()
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
    
    def guess(self, letter):
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")
        
        letter = letter.lower()
        if letter in self.guesses:
            self.remaining_guesses -= 1
        elif letter in self.word:
            self.guesses.add(letter)
        else:
            self.guesses.add(letter)
            self.remaining_guesses -= 1
        
        if all(c in self.guesses for c in set(self.word)):
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE
    
    def get_masked_word(self):
        return "".join(c if c in self.guesses else "_" for c in self.word)
    
    def get_status(self):
        return self.status