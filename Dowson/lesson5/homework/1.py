# вывод списка слов в случайном порядке
import random

words = ["привет", "пока", "стоп", "старт"]
show_word = []
n = 0
while len(show_word) != len(words):
    count = random.randrange(len(words))
    if words[count] in show_word:
        print("пробуем еще раз:")
    else:
        show_word.append(words[count])
    n += 1

print(
    "попыток:\t ", n, 
    "второй список: \t", show_word )
