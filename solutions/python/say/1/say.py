table ={
    1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five",
    6 : "six", 7 : "seven", 8 : "eight", 9 : "nine", 10 : "ten",
    11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen",
    15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen",
    19 : "nineteen", 20 : "twenty", 30 : "thirty", 40 : "forty",
    50 : "fifty", 60 : "sixty", 70 : "seventy", 80 : "eighty", 90 : "ninety"
    }

# Translating (3-1) digit chunks
def num_eng(num : int) -> str:
    build_string = ""
    if num // 100 > 0:
        build_string += table.get(num // 100) + " hundred "
        num -= (num // 100) * 100
    if num // 1 != 0:
        if num > 19:
            build_string += table.get(num // 10 * 10)
            num -= (num // 10) * 10
            if num // 1 != 0:
                build_string += "-" + table.get(num)
        else:
            build_string += table.get(num)
    return build_string

# Main function to translate numbers to english
def say(number : int) -> str:
    # zero and out of range check
    if 0 > number or number > 999_999_999_999:
        raise ValueError("input out of range")
    elif number == 0: return "zero"
    
    # placing 3 digit chunks into a list
    string_num, chunks = str(number), []
    for i in range(len(string_num), 0, -3):
        chunks.append(string_num[max(0, i-3):i])
    
    # list[str] -> integer -> words
    result = ""
    for index, digits in enumerate(chunks):
        digits = int(digits)
        if index == 0 and digits != 0:
            result = num_eng(digits)
        if index == 1 and digits != 0:
            result = num_eng(digits) + " thousand " + result
        if index == 2 and digits != 0:
            result = num_eng(digits) + " million " + result
        if index >= 3 and digits != 0:
            result = num_eng(digits) + " billion " + result

    return result.strip()
