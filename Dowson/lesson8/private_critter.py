# закрытая зверюшка

class Critter(object):
    def __init__(self, name, mood):
        print("Hey! новый питомец")
        self.name = name
        self.__mood = mood
    def talk(self):
        print("Name: ", self.name)
        print("Чувствую себя ", self.__mood, "\n")
    def __privete_method(self):
        print("Закрытый метод")
    def public_method(self):
        print("Открытый метод")
        self.__privete_method()

crit = Critter(name= "Bob", mood= "fine")
crit2 = Critter(name= "cat", mood= "bad")
crit.talk()
crit2.talk()
crit.public_method()