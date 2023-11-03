# Доступ отовсюду
def read_global():
    print(value, "Область видимости в функции read_global")

def shadow_global():
    value = 5
    print(value, "Область видимости в функции shadow_global")

def change_global():
    global value
    value = -500
    print(value, "Область видимости в функции change_global")

value = 100
print("start",value)
read_global()
shadow_global()
change_global()
print("end",value)