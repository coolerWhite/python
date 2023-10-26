# Рекорды 2.0
scores = []
choise = None
while choise != "0":
    print(
    """
    Рекорды:
    0 - Выход
    1 - Показать рекорды
    2 - Добавить рекорды
    """        
    )
    choise = input("Ввести номер: ")
    if choise == "0":
        print("BB Maaaan")
    elif choise == "1":
        print("Рекорд")
        print("Nickname", "\t", "Scope")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    elif choise == "2":
        name = input("Введи свой Ник: ")
        score = int(input("Введи свой счет: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    else:
        print("Not in list this number", choise)