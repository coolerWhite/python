def disemvowel(words):
    vow = "aAeEiIoOuU"
    for i in vow:
        words = words.replace(i, "")
    return words

print(disemvowel("This website is for losers LOL!"))