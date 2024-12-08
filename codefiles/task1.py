from typing import List, Optional

class MatrixKeeper:
    def __init__(self):
        self.matrix: Optional[List[List[float]]] = None

    def inputMatrix(self) -> None:
        """Ввод матрицы
        Первое приглашение - ввод размера матрицы n X m
        Второе приглашение - ввод самой матрицы по строчке, элементы через пробел"""
        
        try:
            n, m = map(int, input("Введите размер матрицы n x m через пробел: ").split())
            self.matrix = []
            print("Введите матрицу по строке, разделяя элементы строки пробелом\n")
            for _ in range(n):
                row = list(map(float, input().split()))
                if len(row) != m:
                    raise ValueError("Количество элементов в строке не соответствует m.")
                self.matrix.append(row)
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            self.matrix = None

    def trace(self) -> float:
        """Поиск следа матрицы"""
        
        if self.matrix is None:
            raise ValueError("Матрица не была введена.")

        if len(self.matrix) != len(self.matrix[0]):
            raise ValueError("Матрица должна быть квадратной для вычисления следа.")

        return sum(self.matrix[i][i] for i in range(len(self.matrix)))

    def findByIndex(self, n: int, m: int) -> float:
        """Находит элемент в матрице по индексу вида n, m и выводит его"""
        
        if self.matrix is None:
            raise ValueError("Матрица не была введена.")

        if n <= 0 or m <= 0 or n > len(self.matrix) or m > len(self.matrix[0]):
            raise IndexError("Индексы выходят за пределы матрицы.")

        return self.matrix[n-1][m-1]

def main():
    matrix_keeper = MatrixKeeper()

    while True:
        print("\nВыберите из предложенных опций:")
        print("1: Ввести матрицу вручную.")
        print("2: Найти след матрицы.")
        print("3: Найти элемент по индексу в заданной матрице.")
        print("4: Выйти из программы.\n")

        try:
            option = int(input("Введите номер соответствующей опции: "))
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.\n")
            continue

        if option == 1:
            matrix_keeper.inputMatrix()
        elif option == 2:
            try:
                trace_value = matrix_keeper.trace()
                print(f"След матрицы: {trace_value}\n")
            except ValueError as e:
                print(e)
        elif option == 3:
            try:
                n = int(input("Введите номер строки: "))
                m = int(input("Введите номер столбца: "))
                element = matrix_keeper.findByIndex(n, m)
                print(f"Элемент матрицы [{n}][{m}] = {element}\n")
            except (ValueError, IndexError) as e:
                print(e)
        elif option == 4:
            print("Выход из программы.\n")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите опцию от 1 до 4.\n")

if __name__ == "__main__":
    main()