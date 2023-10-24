# random latter 
import random
word = "индекс"
print("In var word save word: ", word, "\n")
high = len(word)
low = -len(word)
for i in word:
    pos = random.randrange(low, high)
    print("word[", pos, "]\t", word[pos])
print(low)