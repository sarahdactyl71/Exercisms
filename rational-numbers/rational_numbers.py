from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)
        # The sum of two rational numbers r1 = a1/b1 and r2 = a2/b2
        # is r1 + r2 = a1/b1 + a2/b2 = (a1 * b2 + a2 * b1) / (b1 * b2).

    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)
        # The difference of two rational numbers r1 = a1/b1 and r2 = a2/b2
        # is r1 - r2 = a1/b1 - a2/b2 = (a1 * b2 - a2 * b1) / (b1 * b2).

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)
        # The product (multiplication) of two rational numbers r1 = a1/b1 and r2 = a2/b2
        # is r1 * r2 = (a1 * a2) / (b1 * b2).

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = other.numer * self.denom
        return Rational(numer, denom)
        # Dividing a rational number r1 = a1/b1 by another r2 = a2/b2
        # is r1 / r2 = (a1 * b2) / (a2 * b1) if a2 * b1 is not zero.

    def __abs__(self):
        numer = abs(self.numer)
        denom = abs(self.denom)
        return Rational(numer, denom)
        # The absolute value |r| of the rational number r = a/b is equal to |a|/|b|.

    def __pow__(self, power):
        # Exponentiation of a rational number r = a/b to a non-negative integer
        # power n is r^n = (a^n)/(b^n).
        if power < 0:
            power = -power
            numer = self.denom ** power
            denom = self.numer ** power
            return Rational(numer, denom)
        # Exponentiation of a rational number r = a/b to a negative integer
        # power n is r^n = (b^m)/(a^m), where m = |n|.
        elif isinstance(power, float):
            numer = self.numer ** power
            denom = self.denom ** power
            return Rational(numer, denom)
        else:
            numer = self.numer ** power
            denom = self.denom ** power
            return Rational(numer, denom)
        # Exponentiation of a rational number r = a/b to a real (floating-point)
        # number x is the quotient (a^x)/(b^x), which is a real number.

    def __rpow__(self, base):
        pass

#
# Exponentiation of a real number x to a rational number r = a/b is x^(a/b) = root(x^a, b), where root(p, q) is the qth root of p.
#
# Implement the following operations:
#
# addition, subtraction, multiplication and division of two rational numbers,
# absolute value, exponentiation of a given rational number to an integer power,
# exponentiation of a given rational number to a real (floating-point) power,
# exponentiation of a real number to a rational number.
# Your implementation of rational numbers should always be reduced to lowest
# terms. For example, 4/4 should reduce to 1/1, 30/60 should reduce to 1/2, 12/8
# should reduce to 3/2, etc. To reduce a rational number r = a/b, divide a and b
# by the greatest common divisor (gcd) of a and b. So, for example, gcd(12, 8) = 4,
# so r = 12/8 can be reduced to (12/4)/(8/4) = 3/2.
#
# Assume that the programming language you are using does not have an implementation
# of rational numbers.
