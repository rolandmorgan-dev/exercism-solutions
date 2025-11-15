from itertools import permutations

def solve():
    persons = ("Norwegian", "Englishman", "Ukrainian", "Spaniard", "Japanese")
    hobbies = ("dancing", "reading", "football", "painter", "chess")
    drinks = ("coffee", "tea", "milk", "orange juice", "water")
    colors = ("red", "green", "ivory", "yellow", "blue")
    pets = ("dog", "snail", "fox", "horse", "zebra")

    for person in permutations(persons):
        if person[0] != "Norwegian":
            continue

        for color in permutations(colors):
            if person.index("Englishman") != color.index("red"):
                continue
            if color.index("green") != color.index("ivory") + 1:
                continue
            if abs(person.index("Norwegian") - color.index("blue")) != 1:
                continue

            for drink in permutations(drinks):
                if color.index("green") != drink.index("coffee"):
                    continue
                if person.index("Ukrainian") != drink.index("tea"):
                    continue
                if drink[2] != "milk":
                    continue

                for hobby in permutations(hobbies):
                    if color.index("yellow") != hobby.index("painter"):
                        continue
                    if hobby.index("football") != drink.index("orange juice"):
                        continue
                    if person.index("Japanese") != hobby.index("chess"):
                        continue

                    for pet in permutations(pets):
                        if person.index("Spaniard") != pet.index("dog"):
                            continue
                        if pet.index("snail") != hobby.index("dancing"):
                            continue
                        if abs(hobby.index("reading") - pet.index("fox")) != 1:
                            continue
                        if abs(hobby.index("painter") - pet.index("horse")) != 1:
                            continue

                        water_drinker = person[drink.index("water")]
                        zebra_owner = person[pet.index("zebra")]
                        return water_drinker, zebra_owner

def drinks_water():
    return solve()[0]

def owns_zebra():
    return solve()[1]
