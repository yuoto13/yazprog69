import json
import re
from statistics import mean

# Основная функция для запуска парсера
def main():
    file_path = r'6lab\pp.json'  # Путь к входному файлу
    keys_values, measurements = parse_file(file_path)  # Парсинг файла
    x_avg, y_avg, z_avg = calculate_averages(measurements)  # Вычисление средних значений

    result = {
        "program": keys_values.get("program"),
        "inp file": keys_values.get("inp file", []),
        "obs start": keys_values.get("obs start"),
        "obs end": keys_values.get("obs end"),
        "pos mode": keys_values.get("pos mode"),
        "solution": keys_values.get("solution"),
        "elev mask": keys_values.get("elev mask"),
        "dynamics": keys_values.get("dynamics"),
        "tidecorr": keys_values.get("tidecorr"),
        "ionos opt": keys_values.get("ionos opt"),
        "tropo opt": keys_values.get("tropo opt"),
        "ephemeris": keys_values.get("ephemeris"),
        "navi sys": keys_values.get("navi sys"),
        "amb res": keys_values.get("amb res"),
        "val thres": keys_values.get("val thres"),
        "antenna1": keys_values.get("antenna1"),
        "antenna2": keys_values.get("antenna2"),
        "ref pos": keys_values.get("ref pos"),
        "x_aver": x_avg,
        "y_aver": y_avg,
        "z_aver": z_avg,
        "variant": keys_values.get("variant")
    }
    
    output_path = 'kozlov_kirill.json'  # Название выходного файла
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)  # Сохранение результата в файл JSON
    
    print(f"Результат сохранен в файл {output_path}")  # Вывод сообщения о сохранении файла

# Функция для парсинга файла и извлечения ключей и значений из строк, начинающихся с '%'
def parse_file(file_path):
    keys_values = {}  # Словарь для хранения ключей и значений
    measurements = []  # Список для хранения измерений координат

    with open(file_path, 'r') as file:
        lines = file.readlines()  # Чтение всех строк из файла

    # Проход по каждой строке файла
    for line in lines:
        if line.startswith('%'):  # Проверка, начинается ли строка с '%'
            # Разделение строки на ключ и значение по символу ':'
            key_value = re.split(r'\s*:\s*', line[1:].strip(), maxsplit=1)
            if len(key_value) == 2:  # Проверка, что разделение прошло успешно
                key, value = key_value
                key = key.strip()  # Удаление лишних пробелов из ключа
                value = value.strip()  # Удаление лишних пробелов из значения
                if key not in keys_values:
                    keys_values[key] = value  # Если ключа еще нет в словаре, добавляем его
                else:
                    if not isinstance(keys_values[key], list):
                        keys_values[key] = [keys_values[key]]  # Преобразование значения в список, если ключ уже существует
                    keys_values[key].append(value)  # Добавление нового значения в список
        else:
            # Регулярное выражение для извлечения данных измерений
            match = re.match(r'^(\d{4}/\d{2}/\d{2}\s+\d{2}:\d{2}:\d{2}\.\d{3})\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)\s+(-?\d+\.\d+)', line)
            if match:
                # Добавление извлеченных координат (x, y, z) в список измерений
                measurements.append([float(match.group(i)) for i in range(2, 5)])

    return keys_values, measurements  # Возврат словаря ключей и списка измерений

# Функция для вычисления средних значений координат X, Y и Z
def calculate_averages(measurements):
    x_coords = [m[0] for m in measurements]  # Извлечение всех значений X
    y_coords = [m[1] for m in measurements]  # Извлечение всех значений Y
    z_coords = [m[2] for m in measurements]  # Извлечение всех значений Z
    x_avg = mean(x_coords)  # Вычисление среднего значения X
    y_avg = mean(y_coords)  # Вычисление среднего значения Y
    z_avg = mean(z_coords)  # Вычисление среднего значения Z
    return x_avg, y_avg, z_avg  # Возврат средних значений

if __name__ == "__main__":
    main()  # Запуск основной функции
