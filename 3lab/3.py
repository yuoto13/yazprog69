# Определение функции для вычисления суммы четных элементов на главной диагонали матрицы
def f(matrix) -> int:
    # Определяем размер квадратной подматрицы (минимальный из количества строк и столбцов)
    n = min(len(matrix), len(matrix[0]))

    # Инициализация переменной для накопления суммы четных элементов на диагонали
    s = 0

    # Цикл по элементам на главной диагонали
    for i in range(n):
        # Проверка на четность текущего элемента и его добавление к сумме, если он четный
        if (x := matrix[i][i]) % 2 == 0:
            s += x
    
    # Возвращение суммы четных элементов на главной диагонали
    return s


# Основная функция программы
def main():
    # Пример матрицы
    matrix = [
        [3, 1, 1, 1],
        [1, 2, 1, 1],
        [1, 1, 3, 1],
        [1, 1, 1, 4],
        [1, 1, 1, 1],
    ]

    # Вызов функции для вычисления суммы четных элементов на главной диагонали и вывод результата
    print(f(matrix))


# Проверка, запущена ли программа напрямую (если да, то вызов основной функции)
if __name__ == '__main__':
    main()