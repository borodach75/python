# Подсчёт строк и слов в файле

with open('text5-1.txt', 'r', encoding='utf-8') as my_f:
    countlines = 0
    for line in my_f:
        countlines += 1
        print(f'{countlines} строка. Кол-во слов: {line.count(" ") + 1}')
print('Кол-во строк:', countlines)