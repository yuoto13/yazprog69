def a(n, x):
    if abs(x) >= 1:
        return "Модуль x должен быть меньше 1"

    summ = ((n - 1) * n / 2) * x ** (n - 2)
    return summ
n = 2
x = float(input("Введите значение x: "))

result=a(n, x)
print("Значение выражения равно:",result)