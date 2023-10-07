type_car = input(" Цена марка : ")
car_price = int(input(" Цена авто : "))

tax = float( car_price * 0.1)
insurance = float(car_price * 0.12)
delivery = 64000
diler = float(car_price * 2)
price = car_price + tax + insurance + delivery + diler
print("Общая цена Авто : ", type_car, price )