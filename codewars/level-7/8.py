def min_max(lst):
    min = lst[0]
    max = lst[0]
    for i in lst:
        if i < min:
            min = i
        if i > max:
            max = i
    return [min,max]

print(min_max([1,2,3,4,5]))

count