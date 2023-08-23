import json
import csv

# Чтение данных из JSON-файла
with open('data.json', 'r') as json_file:
    data_dict = json.load(json_file)

# Создание списка данных для CSV
csv_data = []
for id_num, (name, age) in data_dict.items():
    csv_data.append([id_num, name, age, ""])

# Запись данных в CSV-файл
csv_file_path = 'data.csv'
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    # Запись заголовков
    csv_writer.writerow(["ID", "Имя", "Возраст", "Телефон"])
    
    # Запись данных
    csv_writer.writerows(csv_data)

print("Данные успешно записаны в CSV-файл.")
