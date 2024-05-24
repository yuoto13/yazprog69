import re
import json

# Загрузка данных из файла
with open('6lab\pp.json', 'r') as file:
    lines = file.readlines()

# Парсинг метаданных
data_dict = {}
for line in lines:
    if line.startswith('%'):
        line = line.replace('%', '').strip()
        keyv = re.split(r'\s*:\s*', line, maxsplit=1)
        key = keyv[0].strip()
        if len(keyv) > 1:
            value = keyv[1].strip()
            if "(x/y/z-ecef=WGS84,Q=1" not in key:
                if key in data_dict:
                    if isinstance(data_dict[key], list):
                        data_dict[key].append(value)
                    else:
                        data_dict[key] = [data_dict[key], value]
                else:
                    data_dict[key] = value

# Парсинг данных измерений
mea = []
for line in lines:
    if not line.startswith('%'):
        values = line.split()
        if len(values) >= 5 and re.match(r'\d{4}/\d{2}/\d{2}', values[0]):
            mea.append([' '.join(values[0:2])] + values[2:])

# Извлечение координат и расчет средних значений
xv = [float(mea[i][1]) for i in range(len(mea))]
yv = [float(mea[i][2]) for i in range(len(mea))]
zv = [float(mea[i][3]) for i in range(len(mea))]

mx = sum(xv) / len(xv)
my = sum(yv) / len(yv)
mz = sum(zv) / len(zv)

# Формирование результирующего словаря
result_dict = {
    **data_dict,
    "x_aver": mx,
    "y_aver": my,
    "z_aver": mz,
    "variant": 7,
}

# Запись результата в JSON файл с именем кирилл козлов
output_filename = 'kirill_kozlov.json'
with open(output_filename, 'w', encoding='utf-8') as json_file:
    json.dump(result_dict, json_file, ensure_ascii=False, indent=4)
