# Только согласные
message = input("Enter text : ")
new_message = ""
VOWELS = "уеаоэяию"
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print("Create new line: ", new_message)
print("Text without lowels: ", new_message)