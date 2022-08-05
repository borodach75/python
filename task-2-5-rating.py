# Вставка числа в неубывающий набор натуральных чисел

exit_flag = False
while not exit_flag:
    s = list(map(int, input('Введите неубывающий набор натуральных чисел: ').split()))
    for i in range(len(s) - 1):
        if s[i] < s[i + 1]:
            print('Некорректные данные')
            break
    else:
        exit_flag = True
# s = [7, 5, 3, 3, 2]

number = int(input('Введите новый элемент рейтинга: '))
for i, elem in enumerate(s):
    if number > elem:
        s.insert(i, number)
        break
else:
    s.append(number)

print(' '.join(list(map(str, s))))