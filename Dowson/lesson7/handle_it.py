# обработаем
# исключения try\except

try:
    num = float(input("Enter number! "))
except ValueError:
    print("Это не число!!")

# обработка нескольких исключений
for value in (None, "Hi!"):
    try:
        print("Пытаюсь преобразовать в число: ", value, end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Похоже есть косяк")

for value in (None, "Hi!"):
    try:
        print("Пытаюсь преобразовать в число: ", value, end=" ")
        print(float(value))
    except (TypeError):
        print("Похоже есть косяк")
    except (ValueError):
        print("Другой косяк")

# получение аргумента
try:
    num = float(input("Enter number! "))
except ValueError as e:
    print("Похоже есть косяк", e)

# try/except/else

try:
    num = float(input("Enter number! "))
except ValueError:
    print("Похоже есть косяк")
else:
    print("Вы ввели число: ", num)