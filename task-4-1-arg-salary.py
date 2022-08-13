# Расчёт зарплаты через скрипт с аргументами

from sys import argv

try:
    hours, wage, bonus = map(float, argv[1:])
    salary = (hours * wage) + bonus
    print('Выработка в часах:', hours)
    print(f'Ставка в час: {wage:.2f}')
    print(f'Премия: {bonus:.2f}')
    print(f'Заработная плата сотрудника равна: {salary:.2f}')
except ValueError:
    print('Необходимо ввести 3 числовых аргумента: выработка в часах, ставка в час, размер премии')
