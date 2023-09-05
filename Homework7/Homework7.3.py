Рimport json

# Создание словаря
data_dict = {
    123456: ('Alice', 25),
    234567: ('Bob', 30),
    345678: ('Carol', 22),
    456789: ('David', 28),
    567890: ('Eve', 29),
    678901: ('Frank', 31)
}

# Запись словаря в JSON-файл
with open('data.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

print("Словарь успешно записан в JSON-файл.")
