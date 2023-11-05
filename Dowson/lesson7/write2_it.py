text_file = open("write2_it.txt", "w", encoding="utf-8")
line = ["Строка 1\n",
        "Строка 2, а была 3\n",
        "Строка 3\n"]

text_file.writelines(line)
text_file.close()

