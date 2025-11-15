# table of brackets, and their pairs
brackets = ("({[",")}]")

# function to check if every brackets are closed
def is_paired(input_string : str) -> bool:
    # list of unclosed brackets
    missing = []
    for char in input_string:
        # find opening bracket, add it's missing part to the list
        if char in brackets[0]:
            missing.append(brackets[1][brackets[0].index(char)])
        # find closing bracket, remove it from the missing brackets list
        elif char in brackets[1]:
            if missing and missing[-1] == char:
                del missing[-1]
            # no pair for closing bracket = return False
            else: return False

    # if a bracket still missing it's pair = return False
    return len(missing) == 0