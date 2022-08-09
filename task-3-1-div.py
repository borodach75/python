def div_2(var_1, var_2):
    '''Деление двух чисел'''

    try:
        return var_1 / var_2
    except ZeroDivisionError:
        return 'Деление на ноль'

print('Введите первое, а затем второе число')
print(div_2(int(input()), int(input())))
