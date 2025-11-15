allergens=("eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats")

class Allergies:

    def __init__(self, score):
        self.bin = str(bin(score)[2:]).zfill(len(allergens))

    def allergic_to(self, item):
        return bool(int(self.bin[::-1][allergens.index(item)]))

    @property
    def lst(self):
        return [allergens[i] for i, b in enumerate(reversed(self.bin)) if int(b) and i < 8]
