# http://algorytmy.ency.pl/artykul/problem_wydawania_reszty_programowanie_dynamiczne
# http://algorytmy.wmi.amu.edu.pl/wordpress/wp-content/uploads/2011/01/programowanie-dynamiczne.pdf
# https://pl.wikipedia.org/wiki/Problem_wydawania_reszty#Algorytm_z_wykorzystaniem_programowania_dynamicznego


class Cashbox:
    def __init__(self):
        # Cashbox state
        self.cash_register = {}

    def __repr__(self):
        import json
        return json.dumps(self.cash_register, sort_keys=True, indent=4)

    def add(self, cash_register: dict):
        for key in cash_register.keys():
            if key not in self.cash_register:
                self.cash_register[key] = 0
            self.cash_register[key] += int(cash_register[key])

    def reset(self, cash_register: dict):
        self.cash_register = dict(cash_register)

    def payment(self, amount: list):
        for coin in amount:
            if self.cash_register[str(coin)] > 0:
                self.cash_register[str(coin)] -= 1
            else:
                raise ValueError('not enough money in cash register to pay for: %s from %s' % (coin, amount))

    def get_lists_from_dict(self) -> tuple:
        return list(self.cash_register.keys()), list(self.cash_register.values())

    @staticmethod
    def remove_duplicates_from_list(L: list) -> list:
        a = []
        for item in L:
            item = sorted(item)
            if item not in a:
                a.append(item)
        return a

    def is_possible(self, L: list):
        temporary_registry = dict(self.cash_register)
        for coin in L:
            if temporary_registry[str(coin)] > 0:
                temporary_registry[str(coin)] -= 1
            else:
                return False
        return True

    def depth_search_solution(self, amount: int):
        coins, in_register = self.get_lists_from_dict()
        coins = [int(coin) for coin in coins]
        solution = [[coin] for coin in coins]

        # solve
        removable = len(coins)
        while True:
            for i in range(len(solution)):
                for c in range(len(coins)):
                    temp = solution[i] + [coins[c]]
                    # check if adding coin is legal:
                    # check if adding coin will not exceed cash register possibilities
                    if self.is_possible(temp):
                        # if adding coin will not exceed amount
                        if sum(temp) < amount:
                            # add coin to solution
                            solution.append(temp)

                        elif sum(temp) == amount:
                            # if solution was found
                            return temp

            # remove elements from previous iteration
            solution = solution[removable:]

            # if the list is empty, return error
            if not solution:
                return solution

            # remove duplicates
            solution = self.remove_duplicates_from_list(solution)

            # set new removable on new list
            removable = len(solution)

            print(solution)


if __name__ == "__main__":
    # init cashbox
    cashbox = Cashbox()
    cashbox.add({
        '1': 24,
        '4': 3,
        '9': 2
    })

    # test payment
    amount_ = 17
    print('testing payment of %s from cashbox: %s' % (amount_, cashbox))
    solution_ = cashbox.depth_search_solution(amount_)
    print('solution of %s: %s' % (amount_, solution_))

    # test payment on changed cashbox
    cashbox.payment(solution_)
    amount_ = 17
    print('testing payment of %s from cashbox: %s' % (amount_, cashbox))
    solution_ = cashbox.depth_search_solution(amount_)
    print('solution of %s: %s' % (amount_, solution_))

    # reset cashbox
    cashbox.reset({
        '1': 10,
        '2': 2
    })

    # test wrong values
    amount_ = 18
    print('testing payment of %s from cashbox: %s' % (amount_, cashbox))
    solution_ = cashbox.depth_search_solution(amount_)
    print('solution of %s: %s' % (amount_, solution_))
