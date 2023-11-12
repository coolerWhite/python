# зверюшка со свойствами

class Critter(object):
    def __init__(self, name):
        print("Hey! новый питомец")
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя пустое")
        else:
            self.__name = new_name
            print("Имя изменено")

    def talk(self):
        print("Name: ", self.name)

crit = Critter("Bob")
crit.talk()
crit.name = "Kitty"
crit.talk()