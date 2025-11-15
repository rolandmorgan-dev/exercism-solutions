allergens=("eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats")


class Allergies:

    def __init__(self, score):
        self.score = bin(score)[2:].zfill(len(allergens))[::-1]
        self.lst = [allergens[i] for i, b in enumerate(self.score) if int(b) and i < 8]
        
    def allergic_to(self, item):
        return bool(int(self.score[allergens.index(item)]))