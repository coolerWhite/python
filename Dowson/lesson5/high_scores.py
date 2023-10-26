# Рекорды

scores = []
choise = None

while choise != "0":
    print(
    """
    Рекорды:
    0 - Выход
    1 - Показать рекорды
    2 - Добавить рекорды
    3 - Удалить рекорды
    4 - Сортировать список
    """        
    )
    choise = input("Ввести номер: ")
    # выдох из программы
    if choise == "0":
        print("BB guys")
    # вывод списка
    elif choise == "1":
        print("Рекорды")
        for score in scores:
            print(score)
    # добавление элемента в список
    elif choise == "2":
        score = int(input("Новый рекорд рекорд: "))
        scores.append(score)
    # удаление элемента
    elif choise == "3":
        score = int(input("Удалить рекорд: "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "Нет в списке рекордов")
    # сортировка
    elif choise == "4":
        scores.sort(reverse=True)
    else:
        print(choise, "Нет в списке")