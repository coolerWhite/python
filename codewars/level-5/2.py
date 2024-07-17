def pig_it(words):
    word = words.split(" ")
    name = ""
    path = []
    for verb in word:
        if verb.isalpha():
            name = verb.replace(verb[0],"", 1)
            name += verb[0]
            name += "ay"
            path.append(name)
        else:
            path.append(verb)
    return " ".join(path)

print(pig_it('Pig latin is cool !'))

