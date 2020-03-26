# equation solving class and its support functions
from Fraction import Fraction


def sign(x: int) -> str:
    """ return plus or minus sign character, basing on number sign """
    return '+' if (lambda a: (x > 0) - (x < 0)) else '-'


def validate_list(list_: list) -> bool:
    """ validate if list contains only integers """
    return all(isinstance(x, int) for x in list_)


def print_equation(list_: list) -> str:
    """ pretty print equation from list of coefficients """
    equation = ""
    for i in list_:
        power = len(list_) - list_.index(i) - 1
        equation += "%s %sx^%s " % (sign(i), i, power)
    return equation[1:-4].lstrip()


def verify_solution(a: list, x) -> bool:
    """ verifies if 'x' is a solution of equation 'a'"""
    result = 0
    temp = list(a)
    temp.reverse()
    for i in range(len(temp)-1, -1, -1):
        result = result + temp[i] * pow(x, i)
    return result == 0


def find_factors(x: int) -> list:
    """ find positive factors of x """
    factors = []
    for i in range(1, abs(x) + 1):
        if not x % i:
            factors.append(i)
    return factors


def possible_roots(a: list, b: list) -> list:
    """ find a list of possible roots from two lists """
    result = []
    for i in a:
        for j in b:
            result.append(Fraction(i, j))
            result.append(Fraction(j, i))
            result.append(Fraction(-i, j))
            result.append(Fraction(-j, i))
    # remove duplicates
    result = list(set(result))
    # remove non-integer solutions
    result = [x for x in result if x.denominator == 1]
    return result


"""
def return_coefficients_after_divide(poly, root):
    result = poly[0]
    coe = list()
    for i in range(1, len(poly)):
        coe.append(result)
        result = result * root + poly[i]
    return coe


def count_multiplicity(coefficients, root):
    multiplicity = 0
    while True:
        if horner(coefficients, root) != 0 or len(coefficients) == 1:
            return multiplicity
        coefficients = return_coefficients_after_divide(coefficients, root)
        multiplicity += 1
"""


class EquationSolver:
    def __init__(self, a: list = None):
        # equation coefficients
        self.coefficients = []
        if a is not None:
            self.set_equation(a)

    def __repr__(self):
        return print_equation(self.coefficients)

    def set_equation(self, a: list):
        """ set equation of solver object """
        if validate_list(a):
            self.coefficients = a
        else:
            raise ValueError("wrong value fo coefficient")

    def divide_binomial(self, b: list, a: list = None, print_: bool = False) -> tuple:
        """ divide polynomial by binomial with Horner schema """
        # validate equations
        validate_list(b)
        if a is not None:
            self.set_equation(a)

        # divide polynomial by binomial with Horner schema
        result = [self.coefficients[0]]
        for i in range(1, len(self.coefficients)):
            result.append(result[i-1] * -1 * b[-1] + self.coefficients[i])

        # pretty print equation with results
        if print_:
            print("%s = (%s)(%s) + %s" % (
                print_equation(self.coefficients), print_equation(b), print_equation(result[:-1]), result[-1]))

        # return polynomial and the rest from division
        return result[:-1], result[-1]

    def solve(self, a: list = None) -> list:
        """ solve equation and return list of list of solutions and list of their multiplicities:
        [[solutions], [multiplicities]] """
        # validate coefficients
        if a is not None:
            self.set_equation(a)
        else:
            if self.coefficients is None:
                raise TypeError("coefficients not set")

        # solve equation:
        # get list of Fractions that are possible equation roots
        solutions = possible_roots(find_factors(self.coefficients[0]), find_factors(self.coefficients[-1]))

        # verify if solutions are true
        verified_solutions = []
        for solution in solutions:
            if verify_solution(self.coefficients, solution):
                verified_solutions.append(solution)

        # get solutions degrees TODO: get solutions degrees
        multiplicities = []

        # return list of list of solutions and list of their multiplicities: [[solutions], [multiplicities]]
        return [verified_solutions, multiplicities]


if __name__ == "__main__":
    # init EquationSolver
    solver = EquationSolver(a=[2, -6, 4])

    # set new equation
    solver.set_equation(a=[2, 4, -16])

    # print analysed equation
    print(solver)

    # solve equation
    print(solver.solve())

    # divide by binomial
    solver.divide_binomial(b=[1, -2], print_=True)

    # compare example fractions
    print(Fraction(1, 2), Fraction(2, 4), Fraction(1, 2) == Fraction(2, 4))
    print(Fraction(98, 100), Fraction(98, 33), Fraction(98, 100) == Fraction(98, 33))
    print(Fraction(98, 10), Fraction(98, 100), Fraction(98, 10) > Fraction(98, 100))
    print(Fraction(98, 10), Fraction(98, 100), Fraction(98, 10) < Fraction(98, 100))
