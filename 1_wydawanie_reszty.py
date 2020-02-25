# http://algorytmy.ency.pl/artykul/problem_wydawania_reszty_programowanie_dynamiczne
# http://algorytmy.wmi.amu.edu.pl/wordpress/wp-content/uploads/2011/01/programowanie-dynamiczne.pdf
# https://pl.wikipedia.org/wiki/Problem_wydawania_reszty#Algorytm_z_wykorzystaniem_programowania_dynamicznego


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

            possible_return = [0 for _ in range(len(coins))]
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
                if to_return[i] is not 0:
                    print('Trzeba wydać %s sztuk nominału %s' % (to_return[i], coins[i]))


if __name__ == "__main__":
    cashbox = Cashbox()
    cashbox.add_money({
        '1': 10,
        '5': 2,
        '10': 3
    })
    print(cashbox.cash_register)
    cashbox.dynamic_change_request(17)
