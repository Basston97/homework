encoded_str = b'r\xc3\xa9sum\xc3\xa9'

decoded_str_1 = encoded_str.decode('utf-8')

latin1_bytes = decoded_str_1.encode('latin-1')

decoded_str_2 = latin1_bytes.decode('latin-1')

print("Исходная строка в байтах:", encoded_str)
print("Декодированная строка 1:", decoded_str_1)
print("Байты в кодировке 'Latin-1':", latin1_bytes)
print("Декодированная строка 2:", decoded_str_2)
