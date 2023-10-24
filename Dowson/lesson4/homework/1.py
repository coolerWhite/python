# Вывод счета чисел с промежутком
start = int(input("Ввести начало счета: "))
finish = int(input("Ввести конец счета: "))
gap = int(input("Ввести промежуток счета: "))

for i in range(start,finish,gap):
    print(i)