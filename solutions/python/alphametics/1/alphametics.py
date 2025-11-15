from itertools import permutations


def solve(puzzle: str) -> dict[str, int]:
    *additions, summed = puzzle.replace("+", " ").replace("==", " ").split()
    words = additions + [summed]
    letters = set(w for word in words for w in word)

    for numbers in permutations("0123456789", len(letters)):
        mapping = dict(zip(letters, numbers))
        translation = str.maketrans(mapping)
        translated = [w.translate(translation) for w in words]
        
        if any(w[0] == "0" for w in translated):
            continue
        if sum(int(w) for w in translated[:-1]) == int(translated[-1]):
            return {k: int(v) for k, v in sorted(mapping.items())}
    return None