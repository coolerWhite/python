# Законсервируем
# pickle - консервирует объекты данные и сохраняет в файлы
# shelve - произвольный доступ к законсервированным объектам данных
import pickle, shelve

print("Консервация списков")
variety = ["cucumber", "tomato", "cabbage"]
shape = ["loop", "whole", "cube"]
brand = ["val", "mal", "udal"]

f = open("pickles1.dat", "wb")
# запись в бинарном виде
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

print("расКонсервация списков")
f = open("pickles1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety, shape, brand)

print("помещение списков на полку")
s = shelve.open("pickles2.dat")
s["variety"] = ["cucumber", "tomato", "cabbage"]
s["shape"] = ["loop", "whole", "cube"]
s["brand"] = ["val", "mal", "udal"]
s.sync() # проверка что данные записаны

print("\nИзвлечение списка из полки")
print(s["brand"])
print(s["shape"])
print(s["variety"])
s.close()