# Нахождение наибольшую цифры

number = int(input('Введите натуральное число: '))
max_n = 0
while number > 0:
    cyther = number % 10
    if max_n < cyther:
        max_n = cyther
    number //= 10
print('Наибольшая цифра в числе:', max_n)
