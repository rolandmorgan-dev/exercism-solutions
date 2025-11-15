def color_code(color):
    colours = colors(True)
    return colours[color]

def colors(full = False):
    colors = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
    }
    return list(colors.keys()) if full == False else colors