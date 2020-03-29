class Cell:
    def __init__(self, number_of_cells):
        self.number_of_cells = number_of_cells

    def __add__(self, other):
        return Cell(self.number_of_cells + other.number_of_cells)

    def __sub__(self, other):
        if self.number_of_cells - other.number_of_cells > 0:
            return Cell(self.number_of_cells - other.number_of_cells)
        else:
            print('Ошибка операции - резуьтат меньше 0')

    def __mul__(self, other):
        return Cell(self.number_of_cells * other.number_of_cells)

    def __truediv__(self, other):
        return Cell(round(self.number_of_cells + other.number_of_cells))

    def __make_order__(self, cells_in_row: int):
        for itm in range(self.number_of_cells // cells_in_row):
            print('*' * cells_in_row)
        print('*' * (self.number_of_cells % cells_in_row))


cells_1 = Cell(15)
cells_2 = Cell(14)
cells_3 = cells_1 + cells_2
cells_4 = cells_1 - cells_2
cells_5 = cells_1 * cells_2
cells_6 = cells_1 / cells_2
print(cells_3.number_of_cells)
print(cells_4.number_of_cells)
print(cells_5.number_of_cells)
print(cells_6.number_of_cells)
cells_3.__make_order__(5)



