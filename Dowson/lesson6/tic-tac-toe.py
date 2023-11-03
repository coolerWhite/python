# Крестики нолики

X = "X"
O = "O"
EMPTY = " "
TIE = "ничья"
NUM_SQUARES = 9

# Инструкция
def display_instruct():
    print(
        """
        Добро пожаловать на ринг 
        ИИ и человек начинают свою игру
        Выбери число от 0 до 8 и игра начнется
       0 | 1 | 2
       ---------
       3 | 4 | 5
       ---------
       6 | 7 | 8
        """
    )

def ask_yes_no(question):
    response = None
    while response not in("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    go_first = ask_yes_no("Будешь ходить первым? (y/n): ")
    if go_first == "y":
        print("Player 1. START!")
        human = X
        computer = O
    else:
        print("Bot 1. START!")
        computer = X
        human = O
    return computer, human

def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\n\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (0,4,8),
                   (2,4,6)
                   )
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None

def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Choose number: ", 0, NUM_SQUARES)
        if move not in legal:
            print("again!")
    return move

def computer_move(board, computer, human):
    # копируем доску
    board = board[:]
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("Поле", end=" ")
    
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    if turn == X:
        return O 
    else:
        return X
    
def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print(the_winner, "в ряд")
    else:
        print("TIE\n")
    
    if the_winner == human:
        print("Human WINNER!")
    elif the_winner == computer:
        print("Compucter win")
    elif the_winner == TIE:
        print("Ничья")
    
def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
        the_winner = winner(board)
        congrat_winner(the_winner, computer, human)

main()