#импорт
import random

# Считываем целые числа
a1 = int(input("Введите первое целое число: "))
a2 = int(input("Введите второе целое число: "))

# Считываем вещественные числа
x1 = float(input("Введите первое вещественное число: "))
x2 = float(input("Введите второе вещественное число: "))

# Генерируем случайные числа в пределах введенных значений
random_integer = random.randint(min(a1, a2), max(a1, a2))
random_float = random.uniform(min(x1, x2), max(x1, x2))

# Выводим результат
print("Случайное целое число:", random_integer)
print("Случайное вещественное число:", random_float)