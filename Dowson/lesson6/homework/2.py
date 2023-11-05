# отгадай число
import random

def ask_number(question, low, high):
    guess = random.randint(low, high)
    number = 0
    tries = 0
    while number != guess:
        if guess > number:
            print("больше")
        else:
            print("меньше")
        number = int(input(question))
        tries += 1
    return print("Number: ", guess, "Попыток", tries)

min = int(input("min range number: "))
max = int(input("max range number: "))
# tries = int(input("tries: "))

ask_number("Отгадай число: ", min, max)
