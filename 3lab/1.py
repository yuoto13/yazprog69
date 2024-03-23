numbers = []

# Запрос чисел у пользователя
print("Введите числа")
while True:
    num_input = input("Введите число:")
    if num_input == "":
        break
    try:
        num = float(num_input)
        numbers.append(num)
    except ValueError:
        print("Некорректный ввод. Попробуйте еще раз.")

# Поиск наибольшего числа с использованием цикла for
if numbers:
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    # Вывод результата
    print("Наибольшее число в списке:", largest)