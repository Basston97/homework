

def custom_str_to_number(input_str):
    if input_str.startswith('-'):
        if input_str[1:].replace('.', '', 1).isdigit():
            return f"Вы ввели отрицательное число {input_str}."
    elif input_str.replace('.', '', 1).isdigit():
        return f"Вы ввели положительное число {input_str}."
    
    return "Введено неверное число."

# Примеры использования
print(custom_str_to_number("123"))     # Вывод: Вы ввели положительное число 123.
print(custom_str_to_number("-456"))    # Вывод: Вы ввели отрицательное число -456.
print(custom_str_to_number("7.89"))    # Вывод: Вы ввели положительное число 7.89.
print(custom_str_to_number("-0.123"))  # Вывод: Вы ввели отрицательное число -0.123.
print(custom_str_to_number("abc"))  
