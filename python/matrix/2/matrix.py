class Matrix:
    def __init__(self, string):
        self.numbers = [[int(n) for n in nums.split()] for nums in string.splitlines()]

    def row(self, index):
        return self.numbers[index - 1]

    def column(self, index):
        return [col[index - 1] for col in self.numbers]