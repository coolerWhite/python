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
    
    def eat(self):
        # new
        food = int(input("Сколько еды дать?: "))
        if food < 0:
            print("Надо дать еды!")
        if 1 <= food <= 5:
            print("Жадина!")
            self.hunger -= food
        if 6 <= food <= 10:
            print("Нормально!")
            self.hunger -= food
        if 11 < food :
            print("Не перекармливай")
            self.hunger -= food
        else:
            print("Надо что-то выбрать")

        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
    
    def play(self):
        # new
        fun = int(input("Сколько будем играть?: "))
        if fun < 0:
            print("Надо немножко поиграть!")
        if 1 <= fun <= 5:
            print("Мало...")
            self.boredom -= fun
        if 6 <= fun <= 10:
            print("Наигрался!")
            self.boredom -= fun
        if 11 < fun :
            print("Еще..ещё..УСТАЛА!")
            self.boredom -= fun
        else:
            print("Надо что-то выбрать")

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
        1 - Узнать состояние
        2 - Покормить
        3 - Поиграть
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