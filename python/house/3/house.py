table = (
    ("house that Jack built.", "lay in"),
    ("malt", "ate"),
    ("rat", "killed"),
    ("cat", "worried"),
    ("dog", "tossed"),
    ("cow with the crumpled horn", "milked"),
    ("maiden all forlorn", "kissed"),
    ("man all tattered and torn", "married"),
    ("priest all shaven and shorn", "woke"),
    ("rooster that crowed in the morn", "kept"),
    ("farmer sowing his corn", "belonged to"),
    ("horse and the hound and the horn", ""),)

def recite(start, end):
    result = []
    for i in range(start-1,end):
        builder = [f"This is the {table[i][0]}"]
        for noun,verb in reversed(table[:i]):
            builder.append(f"that {verb} the {noun}")
        result.append(" ".join(builder))
    return result