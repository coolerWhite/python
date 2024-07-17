def make_readable(seconds):
    sec = 0
    min = 0
    hour = 0
    count = 0
    while count != seconds:
        count += 1
        sec += 1
        if sec > 59:
            sec = 0
            min +=1
        
        if min > 59:
            min = 0
            hour += 1
            
    return f"{hour:02}:{min:02}:{sec:02}"


print(make_readable(86400))