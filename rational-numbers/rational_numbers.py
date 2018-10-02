from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        gcd, b = sorted([numer, denom])
        while b != 0:
            gcd, b = b, gcd % b
        if denom < 0 < gcd:
            gcd = -gcd
        self.numer = numer // gcd
        self.denom = denom // gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = other.numer * self.denom
        return Rational(numer, denom)

    def __abs__(self):
        numer = abs(self.numer)
        denom = abs(self.denom)
        return Rational(numer, denom)

    def __pow__(self, power):
        if power < 0:
            power = -power
            numer = self.denom ** power
            denom = self.numer ** power
            return Rational(numer, denom)
        elif isinstance(power, float):
            numer = self.numer ** power
            denom = self.denom ** power
            return Rational(numer, denom)
        else:
            numer = self.numer ** power
            denom = self.denom ** power
            return Rational(numer, denom)
    
    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
