import games, random

print("Добро пожаловать")
again = None
while again !=  "n":
    players = []
    num = games.ask_number(question = "Сколько участников? 2-5", low = 2, high = 5)

    for i in range(num):
        name = input("ИМЯ: ")
        score = random.randrange(100)+1
        player = games.Player(name, score)
        players.append(player)
    
    print("Результаты: ")
    for player in players:
        print(player)

again = games.ask_yes_no("Заново?")