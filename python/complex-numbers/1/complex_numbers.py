from math import exp, cos, sin; from numbers import Number

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = self.imaginary = imaginary
    
    def extract_parts(self, value):
        if isinstance(value, Number): return value, 0
        return value.real, value.imag
    
    def __add__(self, other):
        real, imag = self.extract_parts(other)
        return ComplexNumber(self.real + real, self.imag + imag)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        real, imag = self.extract_parts(other)
        return ComplexNumber(self.real - real, self.imag - imag)
    
    def __rsub__(self, other):
        real, imag = self.extract_parts(other)
        return ComplexNumber(real - self.real, imag - self.imag)
    
    def __mul__(self, other):
        real, imag = self.extract_parts(other)
        real_part = self.real * real - self.imag * imag
        imag_part = self.imag * real + self.real * imag
        return ComplexNumber(real_part, imag_part)
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, other):
        real, imag = self.extract_parts(other)
        denom = real ** 2 + imag ** 2 # Denominator for division (magnitude squared)
        real_part = (self.real * real + self.imag * imag) / denom
        imag_part = (self.imag * real - self.real * imag) / denom
        return ComplexNumber(real_part, imag_part)
    
    def __rtruediv__(self, other):
        denom = self.real ** 2 + self.imag ** 2
        real_part = (other * self.real) / denom
        imag_part = (-other * self.imag) / denom
        return ComplexNumber(real_part, imag_part)
    
    def __abs__(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5
    
    def conjugate(self):
        return ComplexNumber(self.real,-self.imag)
    
    def __eq__(self, other):
        # Return False if the other object is not a ComplexNumber
        if not isinstance(other, ComplexNumber): return False
        return self.real == other.real and self.imag == other.imag
    
    def exp(self):
        e = exp(self.real)
        return ComplexNumber(e * cos(self.imag), e * sin(self.imag))