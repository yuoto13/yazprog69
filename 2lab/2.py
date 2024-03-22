import math
x=float(input())
y=float(input())
if x**2+y**2<=1 or 0>=x>=-1 and -1<=y<=1:
    print('Точка лежит на данной фигуре')
else:
    print('Точка не лежит на данной фигуре')