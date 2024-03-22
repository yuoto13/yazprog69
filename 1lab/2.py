def replace_h(input_string):
    # Находим индекс первого и последнего вхождения буквы "h"
    first_index = input_string.find('h')
    last_index = input_string.rfind('h')

    # Если буква "h" найдена в строке
    if first_index != -1:
        # Заменяем все буквы "h", кроме первой и последней, на "H"
        replaced_string = input_string[:first_index + 1] + \
                          input_string[first_index + 1:last_index].replace('h', 'H') + \
                          input_string[last_index:]
        return replaced_string
    else:
        # Если буква "h" не найдена, возвращаем исходную строку
        return input_string

input_string = "hello, hhow are you ?"
result = replace_h(input_string)
print(result)