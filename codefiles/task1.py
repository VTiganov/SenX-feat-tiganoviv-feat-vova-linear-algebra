from typing import List, Optional

class matrixKeeper():
    
    def __init__(self):
        self.matrix: Optional[List[List[float]]] = None

    def inputMatrix(self) -> None:
        """Ввод матрицы
        Первое приглашение - ввод размера матрицы n X m
        Второе приглашение - ввод самой матрицы по строчке, элементы через проблем"""
        
        n, m = map(int, input("Введите размер матрицы n x m: ").split())
        self.matrix = []
        for _ in range(n):
            row = list(map(float, input().split()))
            self.matrix.append(row)

    def trace(self) -> float:
        """Поиск следа матрицы"""
        pass

    def findByIndex(self, n: int, m: int) -> float:
        """Находит элемент в матрице по индексу вида n,m и выводит его"""
        pass