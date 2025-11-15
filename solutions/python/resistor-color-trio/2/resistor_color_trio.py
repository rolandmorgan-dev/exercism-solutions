codes= {"black": "0","brown": "1","red": "2","orange": "3","yellow": "4",
            "green": "5","blue": "6","violet": "7","grey": "8","white": "9",}

def label(colors):
    kiloohms, megaohms, gigaohms = 1000, 1000000, 1000000000
    first, second, third, *_ = colors
    if second == "black" and third == "black":
        return f"{codes[first]} ohms"
    if second != "black" and third == "black":
        resistance = int(codes[first] + codes[second])
        return f"{resistance} ohms"
    
    resistance = int(codes[first] + codes[second] + int(codes[third]) * "0")
    
    if resistance // gigaohms >= 1: return f"{resistance//gigaohms} gigaohms"
    if resistance // megaohms >= 1: return f"{resistance//megaohms} megaohms"
    if resistance // kiloohms >= 1: return f"{resistance//kiloohms} kiloohms"
    return f"{resistance} ohms"