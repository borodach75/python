# Вывод слов с не более, чем 10-ю буквами

s = input('Введите строку из нескольких слов, разделённых пробелами: ').split()
for i, word in enumerate(s):
    print(f'{i + 1}. {word[:10]}')