# Determining whether a credit card number is valid (Luhn formula)
class Luhn:
    def __init__(self, card_number : str):
        self.card_number = card_number

    def valid(self) -> bool:
        number = self.card_number.replace(" ", "")
        if not number.isdigit() or len(number) < 2:
            return False

        summ = 0
        step = 1
        for num in reversed(number):
            num = int(num)
            if step % 2 == 0:
                num *= 2
                if num > 9:
                    num -= 9
            summ += num
            step += 1

        return bool(summ % 10 == 0)
