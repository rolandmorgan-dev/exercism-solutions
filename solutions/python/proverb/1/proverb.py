# Given a list of inputs, generating the relevant proverb
def proverb(*nouns : str, qualifier : str) -> list:
    if not nouns: return []
    qualifier = "" if qualifier is None else qualifier + " "
    result = []
    for i in range(len(nouns)-1):
        result.append(f"For want of a {nouns[i]} the {nouns[i+1]} was lost.")
    result.append(f"And all for the want of a {qualifier}{nouns[0]}.")
    return result
