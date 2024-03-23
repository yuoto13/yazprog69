# Вывод инструкции для ввода коэффициентов квадратного уравнения
print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")

# Ввод коэффициентов a, b и c
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

 # Вычисление дискриминанта
discr = b**2 - 4 * a * c;
print("Дискриминант D = %.2f" % discr)

# Проверка условий и вычисление корней уравнения
if discr > 0:
    import math
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")