def is_isogram(string):
    iso = set()
    return not any(i in iso or iso.add(i) for i in string.lower())
    # if iso in string:
    #     print("True")

is_isogram("Dermatoglyphics")