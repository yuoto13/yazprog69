#ввод
numbers = list(map(int, input("числа через пробел: ").split()))
# Проверяем, что список не пуст
if not numbers:  
    print("пусто тут")
else:
    largest = numbers[0]  # Первый элемент списка присваиваем переменной largest
    for number in numbers:  # Проходим по каждому числу в списке
        if number > largest:  # Если текущее число больше текущего максимального,то
            largest = number  # Обновляем переменную largest значением текущего числа
    print("макс:", largest)  # Выводим максимальное число