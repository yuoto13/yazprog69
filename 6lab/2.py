import json

# Открытие файла для чтения
file_path = '07.json'
output_file_path = 'kk.json'

with open(file_path, "r") as file:
    lines = file.readlines()  # Чтение всех строк файла
    data = dict()  # Инициализация пустого словаря для хранения данных
    array = []  # Инициализация списка для хранения строк данных
    
    # Чтение первых строк с ключ-значение парами
    i = 0
    while lines[i].startswith('%'):
        line = lines[i].split(':', 1)
        if len(line) == 2:
            key = line[0].replace('%', '').strip()  # Удаление символа '%' и лишних пробелов из ключа
            value = line[1].strip()  # Удаление пробелов из значения
            if key in data:
                if not isinstance(data[key], list):
                    data[key] = [data[key]]  # Преобразование значения в список, если это не список
                data[key].append(value)  # Добавление значения в список
            else:
                data[key] = value  # Добавление новой пары ключ-значение
        i += 1
    
    # Пропуск следующих трех ненужных строк
    i += 3
    
    # Инициализация переменных для вычисления среднего значения
    avgx = avgy = avgz = 0
    counter = 0
    
    # Чтение и обработка оставшихся строк с данными
    while i < len(lines):
        line = lines[i].split()
        current_line_data = [item.strip() for item in line if item]  # Очистка элементов строки от пробелов
        if len(current_line_data) > 1:
            datetime = current_line_data[0] + ' ' + current_line_data[1]  # Объединение даты и времени
            array.append([datetime] + current_line_data[2:])  # Формирование списка данных с объединенной датой и временем
            counter += 1
        i += 1
    
    # Вычисление средних значений
    for i in range(counter):
        avgx += float(array[i][1])  # Суммирование значений x
        avgy += float(array[i][2])  # Суммирование значений y
        avgz += float(array[i][3])  # Суммирование значений z
    
    length = len(array)
    if length > 0:
        avgx /= length  # Вычисление среднего значения x
        avgy /= length  # Вычисление среднего значения y
        avgz /= length  # Вычисление среднего значения z
    
    # Обновление данных средних значений
    data.update({"x_aver": avgx})
    data.update({"y_aver": avgy})
    data.update({"z_aver": avgz})
    data.update({"variant": 7})
    
    # Запись результатов в JSON файл
    with open(output_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)  # Запись данных в JSON файл с форматированием

print(f"JSON файл был создан и сохранён по пути: {output_file_path}")
