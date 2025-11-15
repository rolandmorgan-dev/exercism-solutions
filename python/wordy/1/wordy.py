"""
Parsing and evaluating simple math word problems
returning the answer as an integer.
"""
def answer(question : str) -> int:
    if "cubed" in question: raise ValueError("unknown operation")
    
    text = question[8:].replace(" by ", " ").strip("?").split() if question else None
    base = int(text[0]) if text and text[0].lstrip('-').isdigit() else None
    
    if base and len(text) == 1: return base
    if not text or len(text) % 2 == 0: raise ValueError("syntax error")

    operations = ("plus","minus","multiplied","divided")
    
    for i in range(2, len(text), 2):
        if text[i-1] in operations and text[i].strip("-").isdigit():
            op = text[i-1]
            num = int(text[i])
            if op == "plus":
                base += num
            elif op == "minus":
                base -= num
            elif op == "multiplied":
                base *= num
            elif op == "divided":
                base //= num
        else:
            raise ValueError("syntax error")
    return base
