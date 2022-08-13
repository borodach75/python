# Произведение элементов списка, сформированного из четных элементов между 100 и 1000

from functools import reduce

print('Произведение:', reduce(lambda x, y: x * y, range(100, 1001, 2)))
