tolerances= {"grey":"±0.05%", "violet":"±0.1%", "blue":"±0.25%", "green":"±0.5%",
            "brown":"±1%", "red":"±2%", "gold":"±5%", "silver":"±10%"}

codes= {"black": 0,"brown": 1,"red": 2,"orange": 3,"yellow": 4,
        "green": 5,"blue": 6,"violet": 7,"grey": 8,"white": 9,}

resistances= {"gigaohms":1000000000,"megaohms":1000000,"kiloohms":1000}

def resistor_label(colors):
    if len(colors) == 4:
        first, second, third, tolerance = colors
        result = int(f"{codes[first]}{codes[second]}" + "0" * codes[third])
    elif len(colors) == 5:
        first, second, third, fourth, tolerance = colors
        result = int(f"{codes[first]}{codes[second]}{codes[third]}" + "0" * codes[fourth])
    else: return "0 ohms"

    for key, value in resistances.items():
        if result // value >= 1:
            if (result/value).is_integer():
                return f"{result // value} {key} {tolerances[tolerance]}"
            else:
                return f"{result / value} {key} {tolerances[tolerance]}"

    return f"{result} ohms {tolerances[tolerance]}"