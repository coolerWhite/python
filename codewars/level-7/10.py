import math
def find_next_square(sq):
    return (math.sqrt(sq) + 1) ** 2 if (math.sqrt(sq)).is_integer() else -1


print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(319225))
print(find_next_square(15241383936))

print(find_next_square(155))
print(find_next_square(342786627))