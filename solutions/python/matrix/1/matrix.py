class Matrix:
    def __init__(self, matrix_string):
        lists = matrix_string.split("\n")
        strings = [lists[i].split() for i in range(0, len(lists))]
        self.square = [list(map(int, sublist)) for sublist in strings]

    def row(self, index):
        return self.square[index-1]

    def column(self, index):
        return list(*(c for i,c in enumerate(zip(*self.square)) if i == index-1))
