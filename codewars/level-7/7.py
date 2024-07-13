def reverse_letter(st):
    word = ""
    for i in st:
        if i.isalpha():
            word += i
    return word[::-1]

print(reverse_letter("krishan"))
print(reverse_letter("ultr53o?n"))