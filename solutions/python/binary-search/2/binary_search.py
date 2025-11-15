def find(numbers : list, search: int) -> int:
    if search in numbers: return numbers.index(search)
    raise ValueError("value not in array")