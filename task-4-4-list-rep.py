# Элементы без повторений

from random import randint

print('Старый список:', *(old_list := [randint(1, 15) for _ in range(15)]))
print('Новый список:', *(new_list := [x for x in old_list if old_list.count(x) == 1]))
