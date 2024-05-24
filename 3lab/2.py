def calculate_series(x, terms=100):
    if abs(x) >= 1:
        raise ValueError("Абсолютное значение x должно быть меньше 1.")
    
    sum_series = 0
    for n in range(2, terms + 2):
        term = ((n - 1) * n / 2) * (x ** (n - 2))
        sum_series += term
    
    return sum_series

# Запрос значения x у пользователя
try:
    x = float(input("Введите значение x (|x| < 1): "))
    if abs(x) >= 1:
        raise ValueError
    terms = 100  # Количество членов ряда для приближения суммы
    result = calculate_series(x, terms)
    print(f"{result}")
except ValueError:
    print("Вы ввели неверное значение x.")
    exit()