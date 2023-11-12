# зверюшка с конструктором

class Critter(object):
    def __init__(self):
        print("Я родился")
    def talk(self):
        print("Родился питомец")

crit1 = Critter()
crit1.talk()
crit2 = Critter()
crit2.talk()