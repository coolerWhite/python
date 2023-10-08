import random

the_number = int(input("Введите число от 1 до 100 : "))
number = random.randint(0, 100)
tries = 0

while number != the_number:
    tries += 1
    if number > the_number:
        number = random.randint(0, number)
        print(number, "Меньше")
    else:
        number = random.randint(number, 100)
        print(number, "Больше")
    
print(tries)