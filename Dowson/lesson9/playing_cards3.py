#Карты 3.0

class Card(object):
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Unpritable_Card(Card):
    def __str__(self):
        return "нельзя печатать"

class Positionontable_Card(Card):
    def __init__(self, rank, suit, face_up = True):
        super(Positionontable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = super(Positionontable_Card, self).__str__()
        else:
            rep = "XX"
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up

card1 = Card("A", "c")
card2 = Unpritable_Card("A", "d")
card3 = Positionontable_Card("A", "h")
print("Unpritable_Card",card2)
print("Positionontable_Card",card3)
card3.flip()
print("Positionontable_Card",card3)

