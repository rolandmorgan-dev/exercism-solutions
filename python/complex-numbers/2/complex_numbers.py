from math import exp, cos, sin; from numbers import Number

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def extract_parts(self, value):
        if isinstance(value, Number): return value, 0
        return value.real, value.imaginary
    
    def __add__(self, other):
        real, imaginary = self.extract_parts(other)
        return ComplexNumber(self.real + real, self.imaginary + imaginary)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        real, imaginary = self.extract_parts(other)
        return ComplexNumber(self.real - real, self.imaginary - imaginary)
    
    def __rsub__(self, other):
        real, imaginary = self.extract_parts(other)
        return ComplexNumber(real - self.real, imaginary - self.imaginary)
    
    def __mul__(self, other):
        real, imaginary = self.extract_parts(other)
        real_part = self.real * real - self.imaginary * imaginary
        imaginary_part = self.imaginary * real + self.real * imaginary
        return ComplexNumber(real_part, imaginary_part)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        real, imaginary = self.extract_parts(other)
        # Denominator for division (magnitude squared)
        denom = real ** 2 + imaginary ** 2
        real_part = (self.real * real + self.imaginary * imaginary) / denom
        imaginary_part = (self.imaginary * real - self.real * imaginary) / denom
        return ComplexNumber(real_part, imaginary_part)
    
    def __rtruediv__(self, other):
        denom = self.real ** 2 + self.imaginary ** 2
        real_part = (other * self.real) / denom
        imaginary_part = (-other * self.imaginary) / denom
        return ComplexNumber(real_part, imaginary_part)
    
    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5
    
    def conjugate(self):
        return ComplexNumber(self.real,-self.imaginary)
    
    def __eq__(self, other):
        # Return False if the other object is not a ComplexNumber
        if not isinstance(other, ComplexNumber): return False
        return self.real == other.real and self.imaginary == other.imaginary
    
    def exp(self):
        e = exp(self.real)
        return ComplexNumber(e * cos(self.imaginary), e * sin(self.imaginary))