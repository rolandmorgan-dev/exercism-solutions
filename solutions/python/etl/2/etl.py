# Remapping dictionary
def transform(outdated : dict) -> dict:
    # {number: chars} -> {char: number}
    updated = {}
    for key,value in outdated.items():
        for char in value:
            updated[char.lower()] = key
    return updated
