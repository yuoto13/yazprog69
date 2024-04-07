import math

x = float(input("x: "))
y = float(input("y: "))

# Вычисление расстояния от точки (x, y) до центра окружности (0, 0)
distance = math.sqrt(x**2 + y**2)

# Проверка, лежит ли точка внутри окружности (радиус 1)
if distance <= 1:
  print(f"tochka lejit")
else:
  print(f"tochka ne lejit")