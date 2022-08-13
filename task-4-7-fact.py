# Генератор факториала через yield

def fact():
    num, mult = 0, 1
    while True:
        yield mult
        num += 1
        mult *= num

n = input('До какого числа выводим факториалы? ')
if not n.isdigit() or int(n) < 0:
    print('Вводите неотрицательные целые числа')
else:
    [print(f'{i}! = {val}') for i, val in zip(range(int(n) + 1), fact())]
