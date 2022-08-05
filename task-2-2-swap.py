# Обмен соседних элементов в списке

s_list = input('Введите через пробел элементы списка: ').split()
for i in range(0, len(s_list) - 1, 2):
    s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]
print('Итоговый список:', ' '.join(s_list))
