"""
Taking a nested list and returning a single flattened list
with all the values except nil/null.
"""
def flatten(array: list) -> list:
    result = []
    for item in array:
        if isinstance(item, list):
            result.extend(flatten(item))
        elif item != None:
            result.append(item)
    return result