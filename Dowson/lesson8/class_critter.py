# классово верная зверюшка

class Critter(object):
    total = 0
    @staticmethod
    def status():
        print("Всего зверей: ", Critter.total)
    def __init__(self, name):
        print("Родилась еще одна зверюшка")
        self.name = name
        Critter.total += 1

print("Всего зверей", Critter.total)
crit1 = Critter("Bob")
crit2 = Critter("Kitty")
crit3 = Critter("Mesh")
Critter.status()
print(crit1.total)