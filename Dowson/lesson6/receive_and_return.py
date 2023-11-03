# Принимай и возвращай
def display(message):
    print(message)

def give_me_five():
    five = 5
    return five

def ask_yes_no(question):
    response = None
    while response not in("y", "n"):
        response = input(question).lower()
    return response

display("Вам сообщение")

number = give_me_five()
print("Return function:", number)

answer = ask_yes_no("Enter: 'y' or 'n': ")
print("THX for input", answer)