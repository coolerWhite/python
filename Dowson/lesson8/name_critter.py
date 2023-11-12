# зверюшка с именем

class Critter(object):
    def __init__(self, name):
        print("Родился зверь")
        self.name = name
    def __str__(self):
        rep = "Объект класса Ctitter\n"
        rep += "имя: " + self.name + "\n"
        return rep
    def talk(self):
        print("Hey! My name ", self.name, "\n")

crit1 = Critter(name="Bob")
crit1.talk()
crit2 = Critter("Tom")
crit2.talk()
print("crit1 ", crit1)
print("crit1.name ", crit1.name)