#  Determining whether a number is an Armstrong number
def is_armstrong_number(number: int) -> bool:
    digit_count = len(str(number))
    summ = 0
    for i in str(number):
        summ += int(i) ** digit_count
    return summ == number
