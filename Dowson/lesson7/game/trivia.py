# Викторина
# Игра на выбор правильного варианта ответа
import sys
# задание №2
import pickle, shelve

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
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
# задание 1: добавить стоимость вопросов
    point = (next_line(the_file))
    if point:
        point = int(point)

    explanation = next_line(the_file)
    return category, question, answers, correct, point, explanation

def welcome(title):
    print("\t\t", title)

def write_records (name, score):
    record = {name : score}
    print(record)
    f = shelve.open("file_records.txt")
    f[name] = [score]
    f.sync()
    f.close()


def main():
    # задача 2 : вывод списка рекордов
    # f = open("file_records.txt", "r", encoding='utf-8')
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    # извлечение первого блока 
    category, question, answers, correct, point, explanation = next_block(trivia_file)
    while category:
        # вывод вопроса
        print(category)
        print(question)
        for i in range(4):
            print("\t", i+1, "-", answers[i])
        answer = input("Ваш ответ: ")
        if answer == correct:
            print("Da", end=" ")
            score += point
        else:
            print("Net", end=" ")
        print(explanation)
        print("Score: ", score, "\n\n")
        category, question, answers, correct, point, explanation = next_block(trivia_file)
    trivia_file.close()

    # данные об игроке
    print("Ваши очки: ", score)
    name = input("Введите имя игрока: ")
    write_records(name, score)

    print("Это был последний вопрос")

main()