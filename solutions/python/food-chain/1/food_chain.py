A_R = (("fly", "I don't know why she swallowed the fly. Perhaps she'll die."),
       ("spider", "It wriggled and jiggled and tickled inside her.",
        "spider that wriggled and jiggled and tickled inside her"),
       ("bird", "How absurd to swallow a bird!"),
       ("cat", "Imagine that, to swallow a cat!"),
       ("dog", "What a hog, to swallow a dog!"),
       ("goat", "Just opened her throat and swallowed a goat!"),
       ("cow", "I don't know how she swallowed a cow!"),
       ("horse", "She's dead, of course!"))


def center_verse(n):
    verse = []
    for i in range(0, n):
        if n == 7: break
        beasts = (A_R[i+1][0], (A_R[i][2] if i==1 else A_R[i][0]))
        verse.insert(0, "She swallowed the {} to catch the {}.".format(*beasts))
    verse.insert(0, f"{A_R[n][1]}")
    return verse


def recite(start, end):
    verse = []
    for i in range(start-1, end):
        verse.append(f"I know an old lady who swallowed a {A_R[i][0]}.")
        verse.extend(center_verse(i))
        if 0 < i < 7: verse.append(f"{A_R[0][1]}")
        if i < end-1: verse.append("")
    return verse