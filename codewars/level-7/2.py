def smaller(arr):
    return [len([a for a in arr[i:] if a < arr[i]]) for i in range(0, len(arr))]

    new_arr = []
    for i in arr:
        count = 0
        for j in range(i-1):
            count += 1
        
        new_arr.append(count)
    
    return(new_arr)


smaller([5, 4, 3, 2, 1])

