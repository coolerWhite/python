# Генератор статов персонажей
health = 0
strength = 0
agillity = 0
intellect = 0
points = 30

while points > 0:
    print(
        "Выбрать куда вложить очки навыка:\t ", points,
        "\n1 - Здоровье: ", health,
        "\n2 - Сила: ", strength,
        "\n3 - Ловкость: ", agillity,
        "\n4 - Интелект: ", intellect
        )
    choise = input("Введите номер: ")
    if choise == "1":
        grow = int(input("Введите сколько очков хотите потратить: "))
        if grow > points:
            print("Читер, так нельзя!!!")
        else:
            health += grow
            points -= grow
    if choise == "2":
        grow = int(input("Введите сколько очков хотите потратить: "))
        if grow > points:
            print("Читер, так нельзя!!!")
        else:
            strength += grow
            points -= grow
    if choise == "3":
        grow = int(input("Введите сколько очков хотите потратить: "))
        if grow > points:
            print("Читер, так нельзя!!!")
        else:
            agillity += grow
            points -= grow
    if choise == "4":
        grow = int(input("Введите сколько очков хотите потратить: "))
        if grow > points:
            print("Читер, так нельзя!!!")
        else:
            intellect += grow
            points -= grow
    else:
        print("Не правильный выбор")

print(
    "Ваш персонаж:\t ",
    "\n1 - Здоровье: ", health,
    "\n2 - Сила: ", strength,
    "\n3 - Ловкость: ", agillity,
    "\n4 - Интелект: ", intellect
    )