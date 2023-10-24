# Анаграммы

import random

WORDS = ("строка","перевода","предложения","онлайн","текстами","стрелки","направление","электронных")
word = random.choice(WORDS)
correct = word

jumble = ""
while word:
    pos = random.randrange(len(word))
    jumble += word[pos]
    word = word[:pos] + word[(pos + 1):]

print (jumble)
guess = input("\n Введите слово: ")
while guess != correct and guess != "":
    print("Попробуй еще")
    guess = input("\n Введите слово: ")
if guess == correct:
    print("ты Выиграл")
        