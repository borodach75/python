# Вывод типов данных

type_list = [1, 2.0, complex(3, 3), '4', [5], ('6', ), {7}, frozenset('8'),
             {'9': 9}, True, b'11', bytearray(b'12'), None, ZeroDivisionError]

for one in type_list:
    print(type(one))