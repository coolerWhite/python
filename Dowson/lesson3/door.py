import random
door = random.randrange(10)

if door < 3:
    print("close")
elif 7 > door > 3:
    print("same open")
else:
    print("open") 