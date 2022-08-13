# Создать 2 итератора, один генерит целые числа, другой повторяет элементы списка

from itertools import count, cycle

generator1 = count(3, 3)
list1 = [next(generator1) for _ in range(7)]
print(*list1)

generator2 = cycle(list1)
[print(next(generator2), end=' ') for _ in range(50)]
