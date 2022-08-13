# Элементы нового списка, которые больше предыдущих в исходном

from random import randint

print('Старый список:', *(old_list := [randint(1, 300) for _ in range(15)]))
print('Новый список:', *(new_list := [old_list[i] for i in range(1, len(old_list)) if old_list[i] > old_list[i - 1]]))
