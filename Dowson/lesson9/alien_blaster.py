#Гибель пришельца

class Player(object):
    def blast(self, enemy):
        print("Выстрел...")
        enemy.die()

class Alien(object):
    def die(self):
        print("Я ранен. Медиков...")

print("Game Start!")
hero = Player()
invader = Alien()
hero.blast(invader)