# http://algorytmy.ency.pl/artykul/problem_wydawania_reszty_programowanie_dynamiczne
# http://algorytmy.wmi.amu.edu.pl/wordpress/wp-content/uploads/2011/01/programowanie-dynamiczne.pdf
# https://pl.wikipedia.org/wiki/Problem_wydawania_reszty#Algorytm_z_wykorzystaniem_programowania_dynamicznego


class Cashbox:
    def __init__(self):
        # Cashbox state
        self.cash_register = {}

    def add(self, cash_register: dict):
        for key in cash_register.keys():
            if key not in self.cash_register:
                self.cash_register[key] = 0
            self.cash_register[key] += int(cash_register[key])

    def reset(self, cash_register: dict):
        self.cash_register = dict(cash_register)

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
                    # if adding coin will not exceed amount
                    if sum(temp) < amount:
                        # check if adding coin will not exceed cash register possibilities
                        if self.is_possible(temp):
                            # add coin to solution
                            solution.append(temp)

                    elif sum(temp) == amount:
                        # if solution was found
                        return temp

            # remove elements from previous iteration
            solution = solution[removable:]
            removable = len(solution)

            # if the list is empty, return error
            if not solution:
                return solution

            # remove duplicates
            solution = self.remove_duplicates_from_list(solution)

            print(solution)


if __name__ == "__main__":
    cashbox = Cashbox()
    cashbox.add({
        '1': 4,
        '4': 1,
        '9': 2
    })
    amount_ = 17
    print('solution of %s: %s' % (amount_, cashbox.depth_search_solution(amount_)))

    cashbox.reset({
        '1': 10,
        '2': 2
    })
    amount_ = 18
    print('solution of %s: %s' % (amount_, cashbox.depth_search_solution(amount_)))
