## чтение файла 
file_path = 'file.txt'
open_file = open(file_path, 'r')
text = open_file.read()
print(text)
print(len(text))

text_2 = open_file.readlines()
# print(text_2[1])

open_file.close()
