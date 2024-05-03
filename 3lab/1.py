numbers = list(map(int, input("числа через пробел: ").split()))

if not numbers:  # Проверяем, что список не пуст
    print("пусто тут")
else:
    largest = numbers[0]  # Первый элемент списка
    for number in numbers:
        if number > largest:
            largest = number
    print("макс:", largest)
    