num={10 : "Ten", 9 : "Nine", 8 : "Eight", 7 : "Seven", 6 : "Six",
        5 : "Five", 4 : "Four", 3 : "Three", 2 : "Two", 1 : "One", 0 : "no"}

def recite(start, take=1):
    temp = []
    result = []
    for i in range(start, start-take, -1):
        bottle = lambda x: "bottle" if x == 1 else "bottles"
        temp.append([
            f"{num[i]} green {bottle(i)} hanging on the wall,",
            f"{num[i]} green {bottle(i)} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {num[i-1].lower()} green {bottle(i-1)} hanging on the wall."])
    
    for verse in temp:
        result.extend(verse)
        if verse != temp[-1]:
            result.append("")
            
    return result