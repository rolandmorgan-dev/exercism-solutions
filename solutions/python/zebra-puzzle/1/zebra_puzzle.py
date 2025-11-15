from itertools import permutations

# House indices (0 to 4)
houses = range(5)

# Nationalities in order — used to map final result
NATIONALITIES = ('Norwegian', 'Englishman', 'Ukrainian', 'Spaniard', 'Japanese')


def drinks_water():
    solution = solve()
    return NATIONALITIES[solution['Water']]


def owns_zebra():
    solution = solve()
    return NATIONALITIES[solution['Zebra']]


def solve():
    """
    Returns a dictionary mapping 'Water' and 'Zebra' to their house index.
    """
    for colors in permutations(houses):
        red, green, ivory, yellow, blue = colors
        if green - ivory != 1:
            continue

        for nationalities in permutations(houses):
            norway, englishman, ukrainian, spaniard, japanese = nationalities
            if norway != 0:
                continue
            if englishman != red:
                continue

            for pets in permutations(houses):
                dog, fox, snails, horse, zebra = pets
                if spaniard != dog:
                    continue

                for drinks in permutations(houses):
                    coffee, tea, milk, orange, water = drinks
                    if coffee != green:
                        continue
                    if ukrainian != tea:
                        continue
                    if milk != 2:
                        continue

                    for cigs in permutations(houses):
                        old_gold, kools, chesterfields, lucky_strike, parliaments = cigs
                        if old_gold != snails:
                            continue
                        if kools != yellow:
                            continue
                        if abs(chesterfields - fox) != 1:
                            continue
                        if abs(kools - horse) != 1:
                            continue
                        if lucky_strike != orange:
                            continue
                        if parliaments != japanese:
                            continue
                        if abs(norway - blue) != 1:
                            continue

                        # If we reach this point, all constraints are satisfied
                        return {
                            'Water': water,
                            'Zebra': zebra
                        }

    raise ValueError("No solution found")