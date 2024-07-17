def solution(number):
    c = 0
    for i in range(number):
        if i > 0:
            if i % 3 == 0 or i % 5 == 0:
                print(i)
                c += i
    return c
  

print(solution(4))