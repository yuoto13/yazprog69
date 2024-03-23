#Функция центрирует строку в заданном окне.
def center_string(s, w):
    if len(s) >= w:
        return s
    else:
        num_spaces = (w - len(s)) // 2
        return ' ' * num_spaces + s

# Ввод строки и ширины окна с клавиатуры
s = input("Введите строку: ")
w = int(input("Введите ширину окна: "))

# Вывод центрированной строки
centered_string = center_string(s, w)
print(centered_string)
