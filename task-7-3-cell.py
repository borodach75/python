# Органические клетки


class Cell:
    def __init__(self, cell):
        if cell <= 0:
            raise TypeError('Нужно целое положительное число')
        self.cell = cell

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        op_1, op_2 = self.cell, other.cell
        if op_1 > op_2:
            return Cell(op_1 - op_2)
        if op_1 < op_2:
            print('Неудачный порядок клеток. Сначала надо клетку покрупнее.')
        else:
            print('Нулевая клетка в результате операции — нехорошо.')
        return Cell(1)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        op_1, op_2 = self.cell, other.cell
        if op_1 < op_2:
            print('Неудачный порядок клеток. Сначала надо клетку покрупнее.')
            return Cell(1)
        else:
            return Cell(op_1 // op_2)

    def make_order(self, row):
        a = self.cell // row
        return '\n'.join(['*' * row] * (a + 1))[:(self.cell + a)]

cell_1 = Cell(23)
cell_2 = Cell(3)
cell_3 = cell_1 + cell_2    # 26 = 23 + 3
print(cell_3.make_order(4))
print((cell_1 * cell_2).make_order(10))
print((cell_2 / cell_3).make_order(5))
print((cell_3 / cell_2).make_order(5))
print((cell_3 - cell_2 - cell_1).make_order(5))
cell_0 = Cell(0)
