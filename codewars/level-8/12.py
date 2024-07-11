def number_to_pwr(number, p): 
    sum = 1
    for i in range(p):
        sum *= number
    return sum
        
print(number_to_pwr(4, 2))