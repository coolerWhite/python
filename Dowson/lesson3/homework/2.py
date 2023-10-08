# Бросок монетки

import random

eagle = 0
tails = 0
tries = 0
while tries != 100:
    throw = random.randint(1,2)
    if throw == 1:
        eagle += 1
    else:
        tails += 1
    tries += 1
print("Орлов : \t", eagle, "Решка : \t", tails)