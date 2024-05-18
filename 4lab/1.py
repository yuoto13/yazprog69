def qwerty(numbers_input):
    # Разбиваем введенную строку на отдельные числа и преобразуем их в float, затем создаем список
    numbers = list(map(float, numbers_input.split()))
    
    # Вычисляем среднее арифметическое списка чисел или выводим 0, если список пустой
    average = sum(numbers) / len(numbers) if numbers else 0
    
    return average

# Пример использования функции
numbers_input = input("Введите числа через пробел: ")
average = qwerty(numbers_input)
print("Среднее арифметическое:", average)
