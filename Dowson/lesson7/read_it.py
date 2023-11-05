# Прочитаем
# открыть и закрыть файл
text_file = open("read_it.txt", "r", encoding='utf-8')
text_file.close()

# читать по символьно
text_file = open("read_it.txt", "r", encoding='utf-8')
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

# читать файл целиком
text_file = open("read_it.txt", "r", encoding='utf-8')
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

# одна строка по символьно
text_file = open("read_it.txt", "r", encoding='utf-8')
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

# одна строка целиком
text_file = open("read_it.txt", "r", encoding='utf-8')
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

# весь файл в список 
text_file = open("read_it.txt", "r", encoding='utf-8')
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

# перебираю файл построчно
text_file = open("read_it.txt", "r", encoding='utf-8')
for line in text_file:
    print(line)
text_file.close()
#