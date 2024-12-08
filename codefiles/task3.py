from codefiles.task1 import MatrixKeeper
import typing

def determinerOfMatrix() -> float:
    """Считает определитель матрицы
    По тз размер - до 100х100"""
    

def isMatrixInvertable() -> bool:
    """Существует ли матрица, обратная к данной, detA != 0"""
    try:
        det = determinerOfMatrix(matrix_keeper)
        return det != 0
    except ValueError:
        return False