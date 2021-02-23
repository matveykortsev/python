class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.matrix])

    def __add__(self, other):
        result_matrix = []
        for line_1, line_2 in zip(self.matrix, other.matrix):
            result_line = [el_1 + el_2 for el_1, el_2 in zip(line_1, line_2)]
            result_matrix.append(result_line)
        return result_matrix


matrix_1 = Matrix([[4, 5], [0, 4], [53, 69], [7, 2]])
matrix_2 = Matrix([[7, 2], [3, 5], [63, 17], [18, 54]])
print(matrix_1)
print('\n')
print(matrix_2)
print(matrix_1 + matrix_2)


