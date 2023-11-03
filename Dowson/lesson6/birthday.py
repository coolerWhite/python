# День рождения

def birthday(name, age):
    print("С днем рождения: ", name , "Тебе уже!: ", age)

def birthday2(name = "Иванов", age = 1):
    print("С днем рождения: ", name , "Тебе уже!: ", age)

birthday("иванов", 2)

birthday2()
birthday2(name = "ketty", age = 9)
# birthday2(age=б , name = "петя")
birthday2("катя", 209)
birthday2(50, "вася")

