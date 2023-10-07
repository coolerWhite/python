# Ранье (версия с ошибкой)
# ERROR
# car = input( "Затраты на машину: " )
# rent = input( "Затраты на квартиру: " )
# staff = input( "Затраты на прислугу: " )
# rest = input( "Затраты на рестораны: " )
# games = input( "Затраты на компьютерные игры: " )
# total = car + rent + staff + rest + games
# print( "Общие затраты", total )

#fix

car = int(input( "Затраты на машину: " ))
rent = int(input( "Затраты на квартиру: " ))
staff = int(input( "Затраты на прислугу: " ))
rest = int(input( "Затраты на рестораны: " ))
games = int(input( "Затраты на компьютерные игры: " ))
total = car + rent + staff + rest + games
print( "Общие затраты", total )
