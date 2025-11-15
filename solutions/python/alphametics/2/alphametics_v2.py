from itertools import permutations


def solve(puzzle: str) -> dict[str, int]:
    words = puzzle.replace("+", " ").replace("==", " ").split()
    letters = "".join(set(w for word in words for w in word))

    for digits in permutations("0123456789", len(letters)):
        translation = str.maketrans(letters, "".join(digits))
        translated = [w.translate(translation) for w in words]

        if any(w[0] == "0" for w in translated): continue
        if sum(int(w) for w in translated[:-1]) == int(translated[-1]):
            return {k: int(v) for k, v in zip(letters, digits)}

    return None