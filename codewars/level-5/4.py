def rgb(r, g, b):
    if r >= 255:
        r = 255
    elif r <= 0:
        r = 0
    
    if g >= 255:
        g = 255
    elif g <= 0:
        g = 0
    
    if b >= 255:
        b = 255
    elif b <= 0:
        b = 0
    
    return f"{(hex(r)[2:]).upper():>02}{hex(g)[2:].upper():>02}{hex(b)[2:].upper():>02}"


print(rgb(1, 2, 3))