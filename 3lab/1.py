def find_largest(numbers):
    if not numbers:  
        return None  # Если список пуст, возвращаем None
# Первый элемент списка присваиваем переменной largest
    largest = numbers[0] 
# Проходим по каждому числу в списке 
    for number in numbers:  
# Если текущее число больше текущего максимального, то
        if number > largest: 
# Обновляем переменную largest значением текущего числа 
            largest = number  
# Возвращаем максимальное число
    return largest 

# Пример использования функции
numbers = list(map(int, input("Введите числа через пробел: ").split()))
result = find_largest(numbers)
if result is not None:
    print("Максимальное число:", result)
else:
    print("Список пуст.")