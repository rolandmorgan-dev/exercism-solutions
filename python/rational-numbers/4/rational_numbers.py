class Rational:
    def __init__(self, numer : int, denom : int):
        if denom == 0:
            raise ZeroDivisionError("Denominator can't be 0")
        
        if denom < 0:
            numer *= -1
            denom *= -1
        
        # Reduction to lowest terms (Euclidean algorithm)
        x, y = abs(numer), abs(denom)
        while y:
            x, y = y, x % y
        
        self.numer = numer // x
        self.denom = denom // x

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom,
                        self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom,
                        self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        if other.numer == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        return Rational(self.numer * other.denom, other.numer * self.denom)

    def __pow__(self, power):
        if power < 0:
            return Rational(self.denom ** abs(power), self.numer ** abs(power))
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)