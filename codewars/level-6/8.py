def sort_array(source_array):
    sorting = sorted([i for i in source_array if i % 2 != 0])
    count = 0
    for j in range(len(source_array)):
        if source_array[j] % 2 != 0:
            source_array[j] = sorting[count]
            count +=1
    return source_array
    

print(sort_array([5, 3, 1, 8, 0]))