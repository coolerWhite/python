# Переводчик с гикского на русский
geek = {"geeks": "чудаки"}
choise = None

# методы в словаре
#"Метод get()", geek.get(),
print(
    "\nМетод value()", geek.values(),
    "\nМетод keys()", geek.keys(),
    "\nМетод items()", geek.items() 
     )

while choise != "0":
    print(
    """
    Словарь:
    0 - Выход
    1 - Показать перевод
    2 - Добавить запись
    3 - Изменить запись
    4 - Удалить запись
    """        
    )
    choise = input("Ввести номер: ")
    # выдох из программы
    if choise == "0":
        print("BB guys")
    elif choise == "1":
        term = input("что перевести? ")
        if term in geek:
            definition = geek[term]
            print(term, "означает", definition)
    elif choise == "2":
        term = input("что добавить? ")
        if term not in geek:
            definition = input("Введите толкование: ")
            geek[term] = definition
        else:
            print("Такое уже есть!")
    elif choise == "3":
        term = input("что изменить? ")
        if term in geek:
            definition = input("Введите толкование: ")
            geek[term] = definition
        else:
            print(term, "не существует")
    elif choise == "4":
        term = input("что удалить? ")
        if term in geek:
            del geek[term]
        else:
            print(term, "нет в словаре")