# Матрица

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = (len(matrix), len(matrix[0]))

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.matrix) + '\n'

    def __add__(self, other):
        if self.size == other.size:
            return Matrix([[c + d for c, d in zip(a, b)] for a, b in zip(self.matrix, other.matrix)])
        else:
            raise ArithmeticError('Для сложения матрицы должны быть одной размерности. '
                                  f'А эти матрицы имеют размеры {self.size} и {other.size}.')


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [5, 6], [7, 6]])
print(matrix_1)
print(matrix_2)
print(matrix_1 + matrix_2)
print(matrix_1 + matrix_2 + Matrix([[2, 2], [3, 4], [9, 9]]))
matrix_3 = Matrix([[2, 2, 3], [3, 2, 2]])
print(matrix_3)
print(matrix_1 + matrix_3)
