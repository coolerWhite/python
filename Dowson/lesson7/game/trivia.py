# Викторина
# Игра на выбор правильного варианта ответа
import sys
def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("\nНевозможно открыть файл ", file_name, "\nПричина: ", e)
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    # возврат в отфарматированном виде
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line
    
def next_block(the_file):
    # возвращает блок

    category = next_line(the_file)
    quiestion = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        correct = next_line(the_file)
        if correct:
            correct = correct[0]
            explanation = next_line(the_file)
    return category, quiestion, answers, correct, explanation

def welcome(title):
    print("\t\t", title)

def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    # извлечение первого блока 
    category, quiestion, answers, correct, explanation = next_block(trivia_file)
    while category:
        # вывод вопроса
        print(category)
        print(quiestion)
        for i in range(4):
            print("\t", i+1, "-", answers[i])
        answer = input("Ваш ответ: ")
        if answer == correct:
            print("Da", end=" ")
            score += 1
        else:
            print("Net", end=" ")
        print(explanation)
        print("Score: ", score, "\n\n")
        category, quiestion, answers, correct, explanation = next_block(trivia_file)
        trivia_file.close()
        print("Это был последний вопрос")

main()