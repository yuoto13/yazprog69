# Ввод координат точки (x, y)
x, y = map(float, input("Введите координаты x и y через пробел: ").split())

# Проверка условий для точки (x, y)
if (x - 4)**2 + (y - 2)**2 <= 4:  # Проверка, находится ли точка внутри окружности
    if y >= 2:  # Если точка находится выше или на границе y=2
        print('Точка лежит на данной фигуре')
    else:
        if 3 <= x <= 5:  # Если точка находится внутри или на границе отрезка от x=3 до x=5
            print('точка находится внутри или на границе отрезка')
        else:
            print('Точка не лежит на данной фигуре')
else:
    print('Точка не лежит на данной фигуре')