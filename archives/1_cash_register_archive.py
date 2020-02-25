"""
# http://algorytmy.ency.pl/artykul/problem_wydawania_reszty_programowanie_dynamiczne
# http://algorytmy.wmi.amu.edu.pl/wordpress/wp-content/uploads/2011/01/programowanie-dynamiczne.pdf
# https://pl.wikipedia.org/wiki/Problem_wydawania_reszty#Algorytm_z_wykorzystaniem_programowania_dynamicznego


def remove_duplicates_from_list(L: list) -> list:
    a = []
    for item in L:
        item = sorted(item)
        if item not in a:
            a.append(item)
    return a


class Cashbox:
    def __init__(self):
        # Cashbox state
        self.cash_register = {}

        # declare infinity for automate
        self. infinity = float('inf')

        # dynamic matrix for algorithm
        self.dynamic = []

    def add_money(self, cash_register: dict):
        for key in cash_register.keys():
            if key not in self.cash_register:
                self.cash_register[key] = 0
            self.cash_register[key] += int(cash_register[key])

    def get_lists_from_dict(self) -> tuple:
        return list(self.cash_register.keys()), list(self.cash_register.values())

    def is_possible(self, L: list):
        temporary_registry = dict(self.cash_register)
        for coin in L:
            if temporary_registry[str(coin)] > 0:
                temporary_registry[str(coin)] -= 1
            else:
                return False
        return True

    def change_making(self, n: int):
        This function assumes that all coins are available infinitely.
        n is the number to obtain with the fewest coins.
        coins is a list or tuple with the available denominations.

        _, coins = self.get_lists_from_dict()

        m = [[0 for _ in range(n + 1)] for _ in range(len(coins) + 1)]
        for i in range(1, n + 1):
            m[0][i] = float('inf')  # By default there is no way of making change

        for c in range(1, len(coins) + 1):
            for r in range(1, n + 1):
                # Just use the coin coins[c - 1].
                if coins[c - 1] == r:
                    m[c][r] = 1
                # coins[c - 1] cannot be included.
                # Use the previous solution for making r,
                # excluding coins[c - 1].
                elif coins[c - 1] > r:
                    m[c][r] = m[c - 1][r]
                # coins[c - 1] can be used.
                # Decide which one of the following solutions is the best:
                # 1. Using the previous solution for making r (without using coins[c - 1]).
                # 2. Using the previous solution for making r - coins[c - 1] (without
                #      using coins[c - 1]) plus this 1 extra coin.
                else:
                    m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])
        return m[-1][-1]

    def dynamic_change_request(self, amount: int):
        coins, in_register = self.get_lists_from_dict()

        k = len(coins)
        n = len(in_register)

        # dynamic matrix
        self.dynamic = [[self.infinity] * k] * n
        self.dynamic[0] = [0] * k

        # counters
        i, j = 0, 0

        # filling the matrix
        while j < n:
            while i < k:
                if j == 0:
                    # Rozważamy jednoelementowy zbiór nominałów -
                    # jest tylko jedna możliwość wydania kwoty
                    pass

                i += 1
            j += 1

        # foreign code
        i = 0
        possible_changes = list()
        coins = [int(i) for i in coins]
        while i < len(coins) - 1:
            change_copy = amount

            if coins[i] > change_copy:
                i += 1
                continue

            possible_return = [0] * len(coins)
            for j in range(i, len(coins), 1):
                if change_copy is 0:
                    break
                if coins[j] <= change_copy:
                    if in_register[j] == 0:
                        continue
                    else:
                        while coins[j] <= change_copy and in_register[j] != 0:
                            possible_return[j] += 1
                            change_copy -= coins[j]
            possible_changes.append(possible_return)
            i += 1

        to_return = min(possible_changes, key=sum)
        if sum(to_return) == 0:
            print('Nie da się wydać reszty')
        else:
            for i in range(len(coins)):
                while to_return[i] is not 0 and self.cash_register[str(coins[i])] > 0 and amount > 0:
                    print('wydana moneta: %s' % coins[i])
                    self.cash_register[str(coins[i])] -= 1
                    amount -= coins[i]

        if amount > 0:
            self.dynamic_change_request(amount)

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
                    if sum(temp) <= amount:
                        # check if adding coin will not exceed cash register possibilities
                        if self.is_possible(temp):
                            # add coin to solution
                            solution.append(temp)

                    # if solution was found
                    if sum(solution[-1]) == amount:
                        return solution[-1]

            # remove elements from previous iteration
            solution = solution[removable:]
            removable = len(solution)

            # if the list is empty, return error
            if not solution:
                return solution

            # remove duplicates
            solution = remove_duplicates_from_list(solution)
            print(solution)


if __name__ == "__main__":
    cashbox = Cashbox()
    cashbox.add_money({
        '1': 4,
        '4': 1,
        '9': 2
    })

    # cashbox.dynamic_change_request(17)
    # print(cashbox.change_making(17))
    print(cashbox.depth_search_solution(17))
"""