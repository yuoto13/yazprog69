import random

# Генерация случайного трехзначного числа
value = random.randint(100, 999)
print("Число", value, end=" ")

# Вычисление суммы цифр числа
sum_of_digits = sum(int(digit) for digit in str(value))

# Проверка на делимость суммы цифр на 3
if sum_of_digits % 3 == 0:
    print("делится на три без остатка, т.к. сумма цифр в нем", sum_of_digits)
else:
    print("не делится на три без остатка, т.к. сумма цифр в нем", sum_of_digits)