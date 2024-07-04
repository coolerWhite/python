def correct_tail(body, tail):
    sub = body.str(len(body)-len(tail.length))
    if sub == tail:
        return print(True)
    else:
        return print(False)
    
correct_tail("Fox", "x")