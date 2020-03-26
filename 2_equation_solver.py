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
    for i in range(len(list_)):
        power = len(list_) - i - 1
        equation += "%s %sx^%s " % (sign(i), list_[i], power)
    return equation[1:-4].lstrip()


def divide_binomial(a: list, b: list, print_: bool = False) -> tuple:
    """ divide polynomial by binomial with Horner schema """
    # validate equations
    validate_list(a)
    validate_list(b)

    # divide polynomial by binomial with Horner schema
    result = [a[0]]
    for i in range(1, len(a)):
        result.append(result[i-1] * -1 * b[-1] + a[i])

    # pretty print equation with results
    if print_:
        print("%s = (%s)(%s) + %s" % (
            print_equation(a), print_equation(b), print_equation(result[:-1]), result[-1]))

    # return polynomial and the rest from division
    return result[:-1], result[-1]


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
    # sort results
    # result.sort()
    # remove non-integer solutions
    result = [x for x in result if x.denominator == 1]
    return result


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
        if a[-1] == 0:
            raise ValueError("constant term can not be equal to 0")
        if validate_list(a):
            self.coefficients = a
        else:
            raise ValueError("wrong value for coefficient")

    def solve(self, a: list = None) -> list:
        """ solve equation and return list of list of solutions and list of their multiplicities:
        [[solutions], [multiplicities]] """
        # validate coefficients
        if a is not None:
            self.set_equation(a)
        elif self.coefficients is None:
            raise TypeError("coefficients not set")

        # solve equation:
        # get list of Fractions that are possible equation roots
        solutions = possible_roots(find_factors(self.coefficients[0]), find_factors(self.coefficients[-1]))

        # verify if solutions are true
        verified_solutions = []
        for solution in solutions:
            if verify_solution(self.coefficients, solution):
                verified_solutions.append(solution)
        solutions = list(verified_solutions)
        del verified_solutions

        # get solutions degrees
        multiplicities = []

        # for all solutions of equation
        for solution in solutions:
            degree = 0
            equation = list(self.coefficients)

            # divide the equation by solution as long as the resting polynomial's solution is the tested solution
            while True:
                equation, rest = divide_binomial(a=equation, b=[1, -solution])
                if rest != Fraction(0, 1):
                    break
                degree += 1
            multiplicities.append(degree)

        # return list of list of solutions and list of their multiplicities: [[solutions], [multiplicities]]
        return [solutions, multiplicities]


if __name__ == "__main__":
    # init EquationSolver
    solver = EquationSolver(a=[2, -6, 4])

    # set new equation
    solver.set_equation(a=[2, 4, -16])
    # print analysed equation
    print(solver)
    # solve equation
    print(solver.solve())

    # set new equation
    solver.set_equation(a=[1, 2, -13, 4, -30])
    # print analysed equation
    print(solver)
    # solve equation
    print(solver.solve())

    # set new equation
    solver.set_equation(a=[1, -6, 9])
    # print analysed equation
    print(solver)
    # solve equation
    print(solver.solve())

    # set new equation - no integral solutions, solutions should be empty
    solver.set_equation(a=[3, -1, 3, -1])
    # print analysed equation
    print(solver)
    # solve equation
    print(solver.solve())

    # compare example fractions
    print(Fraction(1, 2), Fraction(2, 4), Fraction(1, 2) == Fraction(2, 4))
    print(Fraction(98, 100), Fraction(98, 33), Fraction(98, 100) == Fraction(98, 33))
    print(Fraction(98, 10), Fraction(98, 100), Fraction(98, 10) > Fraction(98, 100))
    print(Fraction(98, 10), Fraction(98, 100), Fraction(98, 10) < Fraction(98, 100))

    # try polynomial with constant term equal to 0
    try:
        solver.set_equation(a=[3, -1, 3, -2, 0])
    except ValueError as e:
        print(e)
