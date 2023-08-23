import csv
from openpyxl import Workbook

# Чтение данных из CSV-файла
csv_file_path = 'data.csv'
csv_data = []

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)  # Пропускаем заголовки
    for row in csv_reader:
        csv_data.append(row[:-1])  # Исключаем столбец с возрастом

# Создание Excel-файла и запись данных
excel_file = Workbook()
sheet = excel_file.active

# Запись заголовков в Excel
sheet.append(headers[:-1])  # Исключаем столбец с возрастом

# Запись данных в Excel
for row in csv_data:
    sheet.append(row)

# Сохранение Excel-файла
excel_file.save('data.xlsx')

print("Данные успешно сохранены в Excel-файл.")
