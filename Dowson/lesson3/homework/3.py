# отгадай число
import random
guess = random.randint(1, 100)
number = int(input("Number : "))
tries = 1
while number != guess:
    if guess > number:
        print("больше")
    else:
        print("меньше")
    number = int(input("Number : "))
    
    tries += 1
    if tries > 5:
        print("You Lose XD")
        break
print(tries, "Попыток")