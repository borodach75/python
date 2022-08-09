def sum2max(*args):
    '''Поиск суммы наибольших 2-х элементов из 3-х'''

    return sum(args) - min(args) if len(args) == 3 else 'Должно быть 3 числа!'

print(sum2max(*map(int, input('Введите через пробел 3 числа: ').split())))

#-----------------------------------------------------------------------------

def sum2max2(arg_1, arg_2, arg_3):
    '''Поиск суммы наибольших 2-х элементов из 3-х'''

    args = [arg_1, arg_2, arg_3]
    return sum(args) - min(args)

try:
    arg_1, arg_2, arg_3 = map(int, input('Введите через пробел 3 числа: ').split())
    print(sum2max2(arg_1, arg_2, arg_3))
except:
    print('Тут какая-то ошибка!')

#-----------------------------------------------------------------------------

sum2max3 = lambda *args: sum(args) - min(args)
print(sum2max3(*map(int, input('Введите несколько через пробел: ').split())))
