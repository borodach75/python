my_power1 = lambda x, y: x ** y

x, y = map(int, input('Введите через пробел x и y: ').split())
print(f'{x} ^ {y} = {my_power1(x, y)}' if x > 0 and y < 0 else 'x должен быть положительным, a y — отрицательным')

#-----------------------------------------------------------------------------

def my_power2(x, y):
    if x <= 0 or y >= 0:
        return 'x должен быть положительным, a y — отрицательным'
    res = 1
    for _ in range(abs(y)):
        res /= x
    return res

x, y = map(int, input('Введите через пробел x и y: ').split())
print(f'{x} ^ {y} = {my_power1(x, y)}' if x > 0 and y < 0 else 'x должен быть положительным, a y — отрицательным')
