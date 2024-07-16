def duplicate_count(text):
    x = []
    t = text.lower()
    for i in t:
        print(i)
        if i not in x:
            if 2 <= t.count(i):
                x.append(i)
    return len(x)


print(duplicate_count("abcdeaB"))

