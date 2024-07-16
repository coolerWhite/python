def array_diff(a, b):
    return [i for i in a if i not in b]
    #     if i in a:
    #         a.remove(i)

    # return var
    #     for j in b:
    #         if i == j:
    #             a.remove(j)
    #             print(a)
    # return a

print(array_diff([1,2,2,3,4,5,6,2], [2]))
