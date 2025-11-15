from random import randint

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)
        
    def roll_dice(self):
        return (randint(1,6) for _ in range(4))
        
    def ability(self):
        return sum(self.roll_dice()) - min(self.roll_dice())

def modifier(value):
    return (value-10) // 2
