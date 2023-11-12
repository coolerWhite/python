class Televisor(object):
    
    def __init__(self):
        print("TV is ON")
        # enter = int(input("влючить телевизор? Enter [y]: "))
        # if enter == "y":
        #     print("TV is ON")
        # else:
        #     print("TV is OFF")

    def Chanel(self, number=6):
         print("Переключил канал на ", number)
    
    def Volume(self):
        choise = input("Выбрать: \n\t1. убавить \n\t2. прибавить")
        vol = 4
        if choise == "1":
            vol_gap = int(input("На сколько убавить? "))
            if vol_gap < 0:
                print("Не верно!")
            else:
                vol -= vol_gap
                print("Убавил звук на: ", vol_gap)

        elif choise == "2":
            vol_gap = int(input("На сколько убвиать? "))
            if vol_gap < 0:
                print("Не верно!")
            elif vol_gap > 100 or vol > 100:
                print("Добавлять больше нельзя", vol)
            else:
                vol += vol_gap
                print("Добавил звук на: ", vol_gap)
        
        return vol
    
    def Shutdown(self):
        print("Телевизор выключен")

def main():
    # tel_name = input("Какая модель телевизора? ")
    tel = Televisor()
    choise = None
    while choise != '0':
        
        print("""
        Выберите действие
        0 - Выключить TV
        1 - Изменить звук
        2 - Поменять канал
        """)

        choise = input("Выбрать действие: ")

        if choise == '0':
            tel.Shutdown()
        if choise == '1':
            tel.Volume()
        if choise == '2':
            tel.Chanel()
        else:
            print("Хорошая шутка")

main()