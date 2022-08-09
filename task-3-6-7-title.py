def int_func(string):
    '''Слово возвращается с заглавной первой буквой и остальными в верхнем регистре'''

    for char in string:
        if not 'a' <= char <= 'z':
            return 'NONE'
    # return string.capitalize()
    return chr(ord(string[0]) - 32) + string[1:]

for word in input('Введите строку из латинских букв в нижнем регистре\n\n').split():
    print(int_func(word), end=' ')