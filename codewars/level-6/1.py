def beggars(values, n):
    return [sum(values[i::n]) for i in range(n)]
#
    result = []
    avg = 0
    values = str(values)
    for i in range(n):
        for j in values[2]:
            avg += int(j)
            print(avg)
        result.append(avg)
    return result

# print(beggars([1,2,3,4,5],1))
# print(beggars([1,2,3,4,5],2))
print(beggars([1,2,3,4,5],3))