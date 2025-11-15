table = ("jump", "close your eyes", "double blink", "wink")

def commands(binary_str):
    binary_list = list(binary_str[1:])
    results = []
    for index, binary in enumerate(binary_list):
        if binary == "1":
            results.append(table[index])
    return  results if binary_str[0]=="1" else results[::-1]