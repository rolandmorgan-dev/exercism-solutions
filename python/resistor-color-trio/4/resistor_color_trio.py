codes= {"black": 0,"brown": 1,"red": 2,"orange": 3,"yellow": 4,
        "green": 5,"blue": 6,"violet": 7,"grey": 8,"white": 9,}

resistances= {"gigaohms":1000000000,"megaohms":1000000,"kiloohms":1000}

def label(colors):
    first, second, third, *_ = colors
    result = int(f"{codes[first]}{codes[second]}" + "0" * codes[third])
    for key, value in resistances.items():
        if result // value >= 1:
            return f"{result // value} {key}"
    return f"{result} ohms"