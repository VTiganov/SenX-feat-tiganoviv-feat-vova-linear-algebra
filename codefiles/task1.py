from typing import List, Optional, Tuple

class MatrixKeeper:
    def __init__(self):
        self.values: Optional[List[float]] = None
        self.indices: Optional[List[int]] = None
        self.indptr: Optional[List[int]] = None
        self.shape: Optional[Tuple[int, int]] = None

    def inputMatrix(self) -> None:
        """Ввод матрицы
        Первое приглашение - ввод размера матрицы n X m
        Второе приглашение - ввод самой матрицы по строчке, элементы через пробел"""

        try:
            n, m = map(int, input("Введите размер матрицы n x m через пробел: ").split())
            self.shape = (n, m)
            self.values = []
            self.indices = []
            self.indptr = [0]
            print("Введите матрицу по строке, разделяя элементы строки пробелом\n")
            for _ in range(n):
                row = list(map(float, input().split()))
                if len(row) != m:
                    raise ValueError("Количество элементов в строке не соответствует m.")
                for j, value in enumerate(row):
                    if value != 0:
                        self.values.append(value)
                        self.indices.append(j)
                self.indptr.append(len(self.values))
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
            self.values = None
            self.indices = None
            self.indptr = None
            self.shape = None

    def trace(self) -> float:
        """Поиск следа матрицы"""

        if self.values is None or self.indices is None or self.indptr is None:
            raise ValueError("Матрица не была введена.")

        if self.shape[0] != self.shape[1]:
            raise ValueError("Матрица должна быть квадратной для вычисления следа.")

        trace_sum = 0
        for i in range(self.shape[0]):
            for idx in range(self.indptr[i], self.indptr[i+1]):
                if self.indices[idx] == i:
                    trace_sum += self.values[idx]
        return trace_sum

    def findByIndex(self, n: int, m: int) -> float:
        """Находит элемент в матрице по индексу вида n, m и выводит его"""

        if self.values is None or self.indices is None or self.indptr is None:
            raise ValueError("Матрица не была введена.")

        if n <= 0 or m <= 0 or n > self.shape[0] or m > self.shape[1]:
            raise IndexError("Индексы выходят за пределы матрицы.")

        for idx in range(self.indptr[n-1], self.indptr[n]):
            if self.indices[idx] == m-1:
                return self.values[idx]
        return 0.0

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
