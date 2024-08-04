def find_uniq(arr):
    mass = arr
    for i in arr:
        if mass.count(i) == 1:
            return i