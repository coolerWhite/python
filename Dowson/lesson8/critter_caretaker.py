# My final Pet

class Critter(object):
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
    
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "fine"
        elif 5<= unhappiness <= 10:
            m = "notbad"
        elif 11 <= unhappiness <= 15:
            m = "не то что бы очень хорошо"
        else:
            m = "terrible"
        return m 
    
    def talk(self):
        print("Мое имя: ", self.name, " чувствую себя ", self.mood, "\n")
        self.__pass_time()
    
    def eat(self, food = 4):
        print("Спасибо за еду")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    
    def play(self, fun = 4):
        print("Lets go!!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("Дайте имя: ")
    crit = Critter(crit_name)
    choise = None

    while choise != '0':
        print("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
        choise = input("Ваш выбор: ")
        print()

        if choise == "0":
            print("See in next time")
        if choise == "1":
            crit.talk()
        if choise == "2":
            crit.eat()
        if choise == "3":
            crit.play()
        else:
            print("Again choise")

main()