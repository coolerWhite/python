# Блэк джек
import cards, games

class BJ_Card(cards.Card):
    ACE_VALUE = 1
    @property
    def value(self):
        # считаем номинал карты
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            # если это не цифра, то значение 10
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

class BJ_Hand(cards.Hand):
    #рука одного игрока
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name
    
    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep
    @property
    def total(self):
        #если одна карта None то и все свойство тоже
        for card in self.cards:
            if not card.value:
                return None
        # суммирукм очки туз = 1
        t = 0
        for card in self.cards:
            t += card.value
        # есть ли туз в руке
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True
        #если туз в руке и сумма очков меньше 11
        if contains_ace and t <= 11:
            t += 10
        return t
    # красиво и элегантно
    def is_busted(self):
        return self.total > 21
    
class BJ_Player(BJ_Hand):
    # игрок
    def is_hitting(self):
        # задание 1
        try:
            response = games.ask_yes_no("\n" + self.name + " , еще карту? (Y/N): ")
        except ValueError:
            print("Увидимся потом!")
        return response == "y"
    def bust(self):
        print(self.name, "перебор")
        self.lose()
    def lose(self):
        print(self.name, "проиграл")
    def win(self):
        print(self.name, "выиграл")
    def push(self):
        print(self.name, "Ничья")

class BJ_Dealer(BJ_Hand):
    def is_hitting(self):
        return self.total < 17
    def bust(self):
        print(self.name, "перебор")
    def flip_first_card(self):
        first_card =self.cards[0]
        first_card.flip()

class BJ_Game(object):
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)
        self.dealer = BJ_Dealer("Dealer")
        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffel()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp
    
    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        #сдача по 2 карты
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()
        
        for player in self.players:
            print(player)
        print(self.dealer)
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()
        
        if not self.still_playing:
            #перебрали все игроки. показать руку дилера
            print(self.dealer)
        else:
            #сдача карт дилеру
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted():
                #выиграли кто остался
                for player in self.still_playing:
                    player.win()
            else:
                #сраниваем, если все вскрываются
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()

def main():
    print("ДОбро пожаловать!!!")
    names = []
    number = games.ask_number("Сколько игроков? (1-7): ", low=1, high=8)
    for i in range(number):
        name = input("ИМЯ: ")
        names.append(name)
        print()
    game = BJ_Game(names)
    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("Продолжаем? ")
        main()

main()