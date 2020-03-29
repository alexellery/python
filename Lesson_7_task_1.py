class Matrix:
    def __init__(self, data):
        self.__data = data

    def __getitem__(self, item):
        return self.__data[item]

    def __iter__(self):
        return self.__data.__iter__()

    def __str__(self):
        return '\n'.join(map(lambda st: ' '.join(map(str, st)), self.__data))

    def __add__(self, other):
        return Matrix(list(map(lambda y: list(map(sum, y)), map(lambda x: list(zip(*x)), zip(self, other)))))


mat_1 = Matrix([[2, 4], [6, 8], [10, 12]])
mat_2 = Matrix([[1, 3], [5, 7], [9, 11]])
mat_3 = mat_1.__add__(mat_2)

print(mat_1.__str__())
print(mat_3)