def digital_root(n):
    count = 0
    for i in str(n):
        count += int(i)

    if len(str(count)) > 1:
        count = digital_root(count)

    return count


    

print(digital_root(16))
print(digital_root(45))
print(digital_root(493193))