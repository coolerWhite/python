#игры

class Player(object):
    def __init__(self, name, scrore = 0):
        self.name = name
        self.score = scrore
    def __str__(self):
        rep = self.name + ":\t" + str(self.score)
        return rep
    
def ask_yes_no(question):
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except ValueError:
            print("Введен не верный символ")
        except KeyboardInterrupt:
            print("CTRL + C =( ")
            break

    return response

if __name__ == "__main__":
    print("запуск модуля напрямую, а не через импорт")
