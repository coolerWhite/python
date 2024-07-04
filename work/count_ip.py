#!/bin/python3
import os

# открыть файл с логом по строчно
file_log = "file.log"
open_file = open(file_log, "r")
text = open_file.readlines()

# словарь куда будет записывать счет IP : количество
diction = {}

# разделение строки. добавления первого элемента в словарь и проверка его количества
for words in text:
    word = words.split()
    # count_ip =+ word[0]
    if word[0] in diction:
        diction[word[0]] += 1
    else:
        diction[word[0]] = 1

# сортировка словаря
dict_sorted = sorted(diction.items(), key=lambda item: item[1], reverse=True)
print(dict_sorted[:3])

open_file.close()