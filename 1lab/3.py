# Ввод данных для первого момента времени
hours1, minutes1, seconds1 = map(int, input("Введите часы, минуты и секунды первого момента времени через пробел: ").split())

# Ввод данных для второго момента времени
hours2, minutes2, seconds2 = map(int, input("Введите часы, минуты и секунды второго момента времени через пробел: ").split())

# Вычисление разницы в секундах между двумя моментами времени
total_seconds1 = hours1 * 3600 + minutes1 * 60 + seconds1
total_seconds2 = hours2 * 3600 + minutes2 * 60 + seconds2
difference_seconds = total_seconds2 - total_seconds1

# Вывод результата
print("Между двумя моментами времени прошло", difference_seconds, "секунд.")