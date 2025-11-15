import re

# Class to format phone numbers and check for errors
class PhoneNumber:
    def __init__(self, number : int):
        
        # Punctuation and letter check
        if re.search(r"[!\"#$%&'*,:;<=>?@[\]^_`{|}~]", number):
            raise ValueError("punctuations not permitted")
        if re.search("[A-Za-z]", number):
            raise ValueError("letters not permitted")
        
        # Placing all numbers in self.number
        self.number = "".join(re.findall("\d+", number))
        
        # 11 digits -> check starting num -> remove it
        if len(self.number) == 11:
            if self.number[0] != "1":
                raise ValueError("11 digits must start with 1")
            self.number = self.number[1:]
        
        # Possible errors block
        checks = (
            (lambda x: len(x) < 10, "must not be fewer than 10 digits"),
            (lambda x: len(x) > 11, "must not be greater than 11 digits"),
            (lambda x: x[0] == "0", "area code cannot start with zero"),
            (lambda x: x[3] == "0", "exchange code cannot start with zero"),
            (lambda x: x[3] == "1", "exchange code cannot start with one"),
            (lambda x: x[0] == "1", "area code cannot start with one"),)
        
        for check, message in checks:
            if check(self.number):
                raise ValueError(message)
        
        # Area code
        self.area_code = self.number[0:3]
        
        # Formatted numbers -> (ddd)-ddd-dddd
    def pretty(self):
        nums = re.search(r'(\d{3})(\d{3})(\d{4})', self.number)
        return '({})-{}-{}'.format(nums.group(1), nums.group(2), nums.group(3))
