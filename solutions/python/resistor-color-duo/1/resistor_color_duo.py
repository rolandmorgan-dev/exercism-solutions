colors = {
    "black": "0",
    "brown": "1",
    "red": "2",
    "orange": "3",
    "yellow": "4",
    "green": "5",
    "blue": "6",
    "violet": "7",
    "grey": "8",
    "white": "9",
    }

def value(colours):
    first, second = colours[0],colours[1]
    return int(colors[first]+colors[second])