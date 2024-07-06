def square_digits(num):
    j = list(map(int, str(num)))
    v = ""
    for i in j:
        i = i*i
        v += str(i)
    return (int(v))

square_digits(9119)