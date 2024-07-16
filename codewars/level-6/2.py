def find_even_index(arr):
    avg = 0
    # return sum(arr[::2])
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1
            


print(find_even_index([1,2,3,4,3,2,1]))
print(find_even_index([1,100,50,-51,1,1]))
print(find_even_index([1,2,3,4,5,6]))