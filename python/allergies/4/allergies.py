class Allergies:
    allergens=("eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats")
    
    def __init__(self, score):
        self.score = bin(score)[2:].zfill(len(self.allergens))[::-1]
        self.lst = [self.allergens[i] for i, b in enumerate(self.score) if int(b) and i < 8]
    
    def allergic_to(self, item):
        return item in self.lst