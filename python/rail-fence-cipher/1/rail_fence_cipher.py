def encode(txt, r):
    grids = create_grids(txt, r-1, 1)
    return "".join(x for row in grids for x in row if x != ".")

def decode(txt, r):
    grids = create_grids(txt, r-1, 0)
    it_txt, r = iter(txt), r-1
    for line in range(len(grids)):
        for char in range(len(grids[0])):
            if grids[line][char] == "?":
                grids[line][char] = next(it_txt)
    return "".join(grids[r - abs(i % (2 * r) - r)][i] for i in range(len(txt)))

def create_grids(txt, r, fill):
    grids = [["."] * len(txt) for _ in range(r+1)]
    for i in range(len(txt)):
        line = r - abs(i % (2 * r) - r)
        grids[line][i] = txt[i] if fill else "?"
    return grids