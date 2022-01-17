"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        my_str = '\n'
        for row in self.matrix:
            for i in row:
                my_str += f'{i:>10}'
            my_str += '\n'
        return my_str

    def __add__(self, other):
        add = []
        if len(self.matrix) != len(other.matrix):
            print("Please, check matrix")
            return
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(other.matrix[i]):
                print('Please, check matrix')
                return None
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            add.append(row)
        return Matrix(add)


m1 = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(f'Matrix1 = {m1}')
m2 = Matrix([[9, 8, 7, 6], [5, 4, 3, 2], [1, 0, -1, -2]])
print(f'Matrix1 = {m2}')
print(f'Matrix1 + Matrix2 = {m1+m2}')
