# Remapping the value of letters
def transform(legacy_data : dict) -> dict:
    result = {}
    for key,value in legacy_data.items():
        for char in value:
            result[char.lower()]=key
    # Sorting letters in ascending order
    result = {k: result[k] for k in sorted(result)}
    return result
