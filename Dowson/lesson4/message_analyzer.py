# Анализатор текста
message = input("Enter you text: ")
print("Length you text:", len(message))
print("More common letter: 'т'")
if "т" in message: # == true / проверка является ли элемент членом последовательности
    print("in text")
else:
    print("not in text")