# Арсенал героя 3
import random

inventory = ["меч", "щит", "броня", "зелье здоровья"]
print("В инвенторе: ", inventory)
print("В твоем инвентаре", len(inventory), "предметов")
if "меч" in inventory:
    print("Готов убить дракона")

index = int(input("Взять предмет под номером(и): "))
print("Взят в руки: ", inventory[index])

chest = ["лук", "зелье маны"]
print("Вы нашли в пещере: \t", chest)
inventory +=chest
print("Теперь в инвенторе: ", len(inventory), "предметов", "\nВсе предметы: ", inventory)

inventory[random.randrange(len(inventory))] = "арбалет"

print("Предметы обновились: ", inventory)

del inventory[random.randrange(len(inventory))]
print("Потерян предмет, текущий инвентарь: ", inventory)

del inventory[random.randrange(len(inventory))]
print("Потерян предмет, текущий инвентарь: ", inventory)

del inventory[random.randrange(len(inventory))]
print("Потерян предмет, текущий инвентарь: ", inventory)