# Implement run-length decoding
def decode(string : str) -> str:
    counter, result = "", ""
    for char in string:
        if char.isdigit():
            counter += char
        elif not char.isdigit():
            if counter.isdigit():
                result += char * int(counter)
                counter = ""
            else: result += char
    return result

# Implement run-length encoding
def encode(string : str) -> str:
    if not string: return string
    result, prev, count = "", string[0], 0
    for i, char in enumerate(string):
        if char == prev: count += 1
        if prev != char and count > 1:
            result += str(count) + prev
            count = 1
        elif prev != char and count == 1:
            result += prev
        if len(string)-1 == i:
            if prev == char and count > 1:
                result += str(count) + prev
            else: result += char
        prev = char
    return result
