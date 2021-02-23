class Cell:
    def __init__(self, cell_nums):
        self.cell_nums = cell_nums

    def __add__(self, other):
        return Cell(self.cell_nums + other.cell_nums)

    def __sub__(self, other):
        return Cell(self.cell_nums - other.cell_nums)

    def __mul__(self, other):
        return Cell(self.cell_nums * other.cell_nums)

    def __truediv__(self, other):
        return Cell(round(self.cell_nums / other.cell_nums))

    def __str__(self):
        return str(self.cell_nums)

    def make_order(self, rows):
       return '\n'.join(['*' * rows for _ in range(self.cell_nums // rows)]) + '\n' + '*' * (self.cell_nums % rows)


cell_1 = Cell(10)
cell_2 = Cell(34)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2.make_order(10))