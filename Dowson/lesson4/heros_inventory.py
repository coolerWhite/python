# Инвентарь героя
# Демонстрация кортежей

inventory = ()
# рассмотрим его как условие

inventory = ("меч",
             "щит",
             "броня",
             "хилка",
             "катана")
print("\n Содержание кортежа: ")
print(inventory)
for item in inventory:
    print(item)
# v2.0
print("\n В инвентаре: ", len(inventory), "предметов")

if "катана" in inventory:
    print("Дорога самурая")
elif "световой меч" in inventory:
    print("Дорога Джедая")
else:
    print("Обычный воин")

index = int(input("Взять предмет(ы): "))
print("Выбраны предметы: ", index, inventory[index])

chest = ("лут", "мантия невидимка")
print("количество найденых предметов", len(chest), "Найдены предметы: ",chest)
print("\n Добавлены в инвентарь")
inventory += chest
print("Предметы в инвентаре", inventory)