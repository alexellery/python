class Worker:
    def __init__(self, name, surname, salary, bonus):
        self._name = name
        self._surname = surname
        self._position = None
        self.__income = {'salary': salary, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'My name is {self._name} {self._surname}.')

    def get_total_payoff(self):
        my_money = self._Worker__income.get('salary') + self._Worker__income.get('bonus')
        print(f'My salary is {my_money}')


me_is = Position('Yamato', 'Kutsutugi', 25000, 10000)

me_is.get_full_name()
me_is.get_total_payoff()