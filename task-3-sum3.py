# Найти сумму чисел n + nn + nnn

number_input = input('Введите натуральное число: ')
n = int(number_input)
nn = int(number_input * 2)
nnn = int(number_input * 3)
print(f'{n} + {nn} + {nnn} = {n + nn + nnn}')
