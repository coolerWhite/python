def solution(a, b):
    result = ""
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a


solution('45', '1')

### return a+b+a if len(a)<len(b) else b+a+b BEST

