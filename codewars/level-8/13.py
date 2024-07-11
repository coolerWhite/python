def are_you_playing_banjo(name):
#1
    return f"{name} plays banjo" if name[0] == name[0].lower() or name[0] == name[0].upper() else f"{name} does not play banjo"
#2
    if name[0] == "r":
        return f"{name} plays banjo"
    elif name[0] == "R":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"





print(are_you_playing_banjo("rolf"))
print(are_you_playing_banjo("Rikke"))