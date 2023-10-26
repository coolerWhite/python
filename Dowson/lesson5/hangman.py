# Виселица
import random
HANGMAN = "ПОВЕШАН"
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("УДАР", "ПЕЧЕНЬ", "НИКТО", "ВЕЧЕН")

# ининциализация переменных 
word = random.choice(WORDS)     # рандомное слово из WORDS
so_far = "-" * len(word)        # дефисы для слова, аля полечудес
wrong = 0                       # число ошибок
used = []                       # отгаданные буквы

print("Player 1. START!")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("Использованные буквы\t\t", used)
    print("Отгаданное слова выглядит так:\t\t", so_far)
    
    guess = input("Ваша буква: ")
    guess = guess.upper()
    while guess in used:
        print("Эта буква уже есть", guess)
        guess = input("Ваша буква: ")
        guess = guess.upper()
    used.append(guess)

    if guess in word:
        print(guess, "Есть в слове")
        # новая so_far строка с отгаданной буквой
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print(guess, "В слове нет")
        wrong += 1
    

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
else:
    print(word, "Было отгадано")