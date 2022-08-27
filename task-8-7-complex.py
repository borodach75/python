# Создание класса «Комплексное число»


class Complex_Number:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @classmethod
    def set(cls, string):
        try:
            if string[0] == '(' and string[-1] == ')':
                string = string[1:-1]
            if string[-1] == 'j':
                pos = string.find('+')
                if pos == -1:
                    pos = string.rfind('-')
                    if pos in (-1, 0):
                        return cls(0, int(string[:-1]))
                a, b = int(string[:pos]), int(string[pos:-1])
            else:
                a, b = int(string), 0
            return cls(a, b)
        except ValueError:
            print('Некорретные данные')

    def __add__(self, other):
        return Complex_Number(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex_Number(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        a, b = self.a, self.b
        c, d = other.a, other.b
        return Complex_Number(a * c - b * d, a * d + b * c)

    def __str__(self):
        return f'({self.a}+{self.b}j)' if self.b > 0 else f'({self.a}{self.b}j)' if self.b < 0 else f'{self.a}'


x = Complex_Number(2, 3)
y = Complex_Number(0, -3)
print(x + y)
print(x * y)
z = Complex_Number.set('-5-7j')
print(z)
