table = (("","horse and the hound and the horn"),
("belonged to","farmer sowing his corn"),
("kept","rooster that crowed in the morn"),
("woke","priest all shaven and shorn"),
("married","man all tattered and torn"),
("kissed","maiden all forlorn"),
("milked","cow with the crumpled horn"),
("tossed","dog"),
("worried","cat"),
("killed","rat"),
("ate","malt"),
("lay in","house that Jack built."))

# Process of placing a phrase of clause within another phrase
def recite(start: int, end: int) -> list:
    result = []
    for i in range(-start, -end-1, -1):
        builder = [f"This is the {table[i][1]}"]
        for a,b in reversed(table[-1:i:-1]):
            builder.append(f"that {a} the {b}")
        result.append(" ".join(builder))
    return result