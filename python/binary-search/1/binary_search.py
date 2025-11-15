def find(search_list, value):
    for index, item in enumerate(search_list):
        if item == value: return index
    raise ValueError("value not in array")