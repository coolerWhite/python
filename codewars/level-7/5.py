def generator(a):
    # yield (a * i for i in range(1,11))
#1
    for i in range(1,a):
        yield f'1 x { a * i } = { a * i }'
    b = 1
#2
    while b < a:
        yield f'1 x { b } = { a * b }'
        b += 1

gen = generator(7)
for j in gen:
    print(j)
