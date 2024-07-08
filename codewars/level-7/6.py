def sequence_sum(begin_number, end_number, step):
#1
    j = 0
    for i in range(begin_number,end_number+1,step):
        j = j + i
    return j
#2
    return sum(range(begin_number,end_number+1,step))

print(sequence_sum(2, 6, 2))