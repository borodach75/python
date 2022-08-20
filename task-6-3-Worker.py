# Worker

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())

manager_1 = Position('Кола', 'Бельды', 'Менеджер', 20000, 5000)
print(manager_1.position, manager_1.get_full_name())
print('Доход:', manager_1.get_total_income())
