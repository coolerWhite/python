# запись

text_file = open("write_it.txt", "w", encoding='utf-8')
text_file.write("Строка 1\n")
text_file.write("Это строка 2\n")
text_file.write("3 Строка в файле\n")
text_file.close()

text_file = open("write_it.txt", "r", encoding='utf-8')
print(text_file.read())
text_file.close()