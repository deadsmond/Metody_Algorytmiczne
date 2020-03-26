from math import gcd


def nth_root(num: int, root: int) -> float:
    return num ** (1/root)


def simplify_fraction(numerator: int, denominator: int):
    comm_div = gcd(int(numerator), int(denominator))
    numerator /= comm_div
    denominator /= comm_div

    return Fraction(int(numerator), int(denominator))


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        """ called on Fraction(numerator, denominator) """
        # reduce fraction
        comm_div = gcd(numerator, denominator)
        numerator /= comm_div
        denominator /= comm_div

        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __repr__(self):
        """ called on repr(), has to return representation with str"""
        return "%s/%s" % (self.numerator, self.denominator)

    def __abs__(self):
        """ called on 'abs(self)' operation """
        return Fraction(abs(self.numerator), abs(self.denominator))

    def __index__(self):
        """ called on 'int(self)' operation """
        if self.denominator == 1:
            return self.numerator
        if self.numerator == 0:
            return 0
        return Fraction(self.numerator, self.denominator)

    def __add__(self, other):
        """ called on 'self + other' operation """
        if isinstance(other, int):
            other = Fraction(other, 1)

        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator

        return simplify_fraction(new_numerator, new_denominator)

    def __radd__(self, other):
        """ called on 'other + self' operation """
        return self.__add__(other)

    def __sub__(self, other):
        """ called on 'self - other' operation, equal to - other + self """
        return self.__add__(-other)

    def __rsub__(self, other):
        """ called on 'other - self' operation, equal to - self + other """
        self.numerator *= -1
        return self.__add__(other)

    def __mul__(self, other):
        """ called on 'self * other' operation """
        if isinstance(other, int):
            other = Fraction(other, 1)

        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator

        return simplify_fraction(new_numerator, new_denominator)

    def __rmul__(self, other):
        """ called on 'other * self' operation """
        return self.__mul__(other)

    def __truediv__(self, other):
        """ called on 'self / other' operation, equal to multiplication of self by inversion of other """
        return self.__mul__(Fraction(other.denominator, other.numerator))

    def __rtruediv__(self, other):
        """ called on 'other / self' operation, equal to multiplication of other by inversion of self """
        self.numerator, self.denominator = self.denominator, self.numerator
        return self.__mul__(other)

    def __iadd__(self, other):
        """ called on 'self += other' operation """
        self.set_self(self.__add__(other))

    def __imul__(self, other):
        """ called on 'self *= other' operation """
        self.set_self(self.__mul__(other))

    def __isub__(self, other):
        """ called on 'self *= other' operation """
        self.set_self(self.__sub__(other))

    def __itruediv__(self, other):
        """ called on 'self *= other' operation """
        self.set_self(self.__truediv__(other))

    def __eq__(self, other) -> bool:
        """ called on 'self is other' operation """
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __hash__(self):
        """ used to make class hashable and thus sorting and duplicate removal possible """
        return hash(str(self))

    def __pow__(self, other):
        """ called on 'pow(self, other)' operation """
        if isinstance(other, int):
            return simplify_fraction(pow(self.numerator, other), pow(self.denominator, other))

        elif isinstance(other, Fraction):
            _ = Fraction(pow(self.numerator, other.numerator), pow(self.denominator, other.numerator))
            return simplify_fraction(
                int(nth_root(_.numerator, other.denominator)), int(nth_root(_.denominator, other.denominator)))

    def set_self(self, other):
        """ used to set self to other values """
        self.numerator = other.numerator
        self.denominator = other.denominator
