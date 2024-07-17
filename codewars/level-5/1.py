def move_zeros(lst):
    ar = []
    for i in lst:
        if i == 0:
            lst.remove(i)
            lst.append(i)
    return lst

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))