from typing import List, Optional
from codefiles.task1 import MatrixKeeper

def matrixAddition(matrix_keeper1: MatrixKeeper, matrix_keeper2: MatrixKeeper) -> Optional[List[List[float]]]:
    """Сложение двух матриц"""

    if matrix_keeper1.matrix is None or matrix_keeper2.matrix is None:
        raise ValueError("Одна или обе матрицы не были введены.")

    if len(matrix_keeper1.matrix) != len(matrix_keeper2.matrix) or len(matrix_keeper1.matrix[0]) != len(matrix_keeper2.matrix[0]):
        raise ValueError("Матрицы должны быть одного размера для сложения.")

    result = []
    for i in range(len(matrix_keeper1.matrix)):
        row = []
        for j in range(len(matrix_keeper1.matrix[0])):
            row.append(matrix_keeper1.matrix[i][j] + matrix_keeper2.matrix[i][j])
        result.append(row)

    return result

def matrixByMatrixMultiplication(matrix_keeper1: MatrixKeeper, matrix_keeper2: MatrixKeeper) -> Optional[List[List[float]]]:
    """Умножение матрицы на матрицу"""

    if matrix_keeper1.matrix is None or matrix_keeper2.matrix is None:
        raise ValueError("Одна или обе матрицы не были введены.")

    if len(matrix_keeper1.matrix[0]) != len(matrix_keeper2.matrix):
        raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы.")

    result = [[0 for _ in range(len(matrix_keeper2.matrix[0]))] for _ in range(len(matrix_keeper1.matrix))]
    for i in range(len(matrix_keeper1.matrix)):
        for j in range(len(matrix_keeper2.matrix[0])):
            for k in range(len(matrix_keeper2.matrix)):
                result[i][j] += matrix_keeper1.matrix[i][k] * matrix_keeper2.matrix[k][j]

    return result

def matrixScalarMultiplication(matrix_keeper: MatrixKeeper, scalar: float) -> Optional[List[List[float]]]:
    """Умножение матрицы на скаляр"""

    if matrix_keeper.matrix is None:
        raise ValueError("Матрица не была введена.")

    result = []
    for row in matrix_keeper.matrix:
        result.append([element * scalar for element in row])

    return result

def main():
    matrix_keeper1 = MatrixKeeper()
    matrix_keeper2 = MatrixKeeper()

    while True:
        print("\nВыберите из предложенных опций:")
        print("1: Ввести первую матрицу вручную.")
        print("2: Ввести вторую матрицу вручную.")
        print("3: Сложить две матрицы.")
        print("4: Умножить матрицу на матрицу.")
        print("5: Умножить матрицу на скаляр.")
        print("6: Выйти из программы.\n")

        try:
            option = int(input("Введите номер соответствующей опции: "))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.\n")
            continue

        if option == 1:
            matrix_keeper1.inputMatrix()
        elif option == 2:
            matrix_keeper2.inputMatrix()
        elif option == 3:
            try:
                result = matrixAddition(matrix_keeper1, matrix_keeper2)
                print("Результат сложения матриц:")
                for row in result:
                    print(row)
            except ValueError as e:
                print(e)
        elif option == 4:
            try:
                result = matrixByMatrixMultiplication(matrix_keeper1, matrix_keeper2)
                print("Результат умножения матриц:")
                for row in result:
                    print(row)
            except ValueError as e:
                print(e)
        elif option == 5:
            try:
                matrix_choice = int(input("Выберите матрицу для умножения на скаляр (1 - первая матрица, 2 - вторая матрица): "))
                if matrix_choice == 1:
                    matrix_keeper = matrix_keeper1
                elif matrix_choice == 2:
                    matrix_keeper = matrix_keeper2
                else:
                    raise ValueError("Некорректный выбор матрицы.")

                scalar = float(input("Введите скаляр: "))
                result = matrixScalarMultiplication(matrix_keeper, scalar)
                print("Результат умножения матрицы на скаляр:")
                for row in result:
                    print(row)
            except ValueError as e:
                print(e)
        elif option == 6:
            print("Выход из программы.\n")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите опцию от 1 до 6.\n")

if __name__ == "__main__":
    main()
