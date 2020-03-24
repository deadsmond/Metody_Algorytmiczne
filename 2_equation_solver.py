# equation solving class and its support functions


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


def verify_solution(a: list, x: int) -> bool:
    result = 0
    a.reverse()
    for i in range(len(a)-1, -1, -1):
        result += a[i] * pow(x, i)
    return result == 0


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

        # return list of list of solutions and list of their multiplicities: [[solutions], [multiplicities]]
        return []


if __name__ == "__main__":
    # init EquationSolver
    solver = EquationSolver(a=[2, -6, 4])

    # print analysed equation
    print(solver)

    # set new equation
    solver.set_equation(a=[1, 0, -9, 3, -5])

    # print analysed equation
    print(solver)

    # divide by binomial
    solver.divide_binomial(b=[1, 7], print_=True)

    print(verify_solution([2, 4, -16], 2))
