from codefiles.task1 import MatrixKeeper
from typing import List

def determinerOfMatrix(matrix_keeper: MatrixKeeper) -> float:
    """Вычисляет определитель матрицы. Размер матрицы: до 100x100."""
    if matrix_keeper.matrix is None:
        raise ValueError("Матрица не задана.")
    
    matrix = matrix_keeper.matrix
    if len(matrix) != len(matrix[0]):
        raise ValueError("Определитель можно вычислить только для квадратной матрицы.")
    
    return gauss(matrix)

def isMatrixInvertable(matrix_keeper: MatrixKeeper) -> bool:
    """Проверяет, существует ли обратная матрица (detA != 0)."""
    try:
        det = determinerOfMatrix(matrix_keeper)
        return det != 0
    except ValueError:
        return False

def gauss(matrix: List[List[float]]) -> float:
    """Вычисляет определитель матрицы методом Гаусса."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]  # Для матрицы 1x1
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]  # Для матрицы 2x2

    swap_count = 0

    for i in range(n):
        max_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))
        if matrix[max_row][i] == 0:
            raise ValueError("Матрица вырожденная, определитель равен нулю.")
        
        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            swap_count += 1

        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]

    determinant = 1.0
    for i in range(n):
        determinant *= matrix[i][i]

    return (-1) ** swap_count * determinant