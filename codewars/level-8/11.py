def find_average(numbers):
    return 0 if numbers == None else sum(numbers) // len(numbers)

print(find_average([1, 2, 3]))