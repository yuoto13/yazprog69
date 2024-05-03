def ya_ystal(matrix):
    if not matrix:
        return 0
    
    #переменная для хранения суммы элементов на главной диагонали
    ya_ystal = 0

    #индексы строки и столбца
    for i in range(len(matrix)):
        # Добавляем элемент на главной диагонали к сумме
        ya_ystal += matrix[i][i]

    return ya_ystal

# матрица моя для примера
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Можно не отвечать на вопросы:):", ya_ystal(matrix))