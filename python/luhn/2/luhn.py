# Determining whether a credit card number is valid (Luhn formula)
class Luhn:
    def __init__(self, card_number : str):
        self.card_number = card_number
        
    def valid(self) -> bool:
        number = self.card_number.replace(" ", "")
        if not number.isdigit() or len(number) < 2:
            return False
        
        summ = 0
        for index, num in enumerate(reversed(number)):
            num = int(num)
            if index % 2 == 0:
                summ += num
            else:
                summ += num * 2 if num < 5 else num * 2 - 9
                
        return bool(summ % 10 == 0)
