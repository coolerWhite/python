def check_exam(arr1,arr2):
    result = 0
    for i in range(len(arr1)):
        if (arr1[i] == arr2[i]):
            result += 4
        elif arr2[i] == "":
            result += 0
        else:
            result -= 1
    
    return 0 if result < 0 else result


print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
print(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]))
print(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]))
print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]))