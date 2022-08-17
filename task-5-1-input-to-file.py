# Запись данных, введённых пользователем, в файл

print('Введите несколько строк данных. Конец для ввода — пустая строка')
with open('text5-1.txt', 'w', encoding='utf-8') as my_f:
    while line := input():
        my_f.write(line + '\n')