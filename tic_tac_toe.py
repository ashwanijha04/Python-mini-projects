#The tic-tac-toe game!
#Instructions

X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instructions():
 #  Displaying game Instructions.
    print("""
        Welcome to Tic-Tac-Toe, a showdown between a Human Brain and an
        Intelligent Computer.
        Brace yourself, human. The battle is on!
            Choose the moves like this.
                0 | 1 | 2
                __________
                3 | 4 | 5
                ----------
                6 | 7 | 8
    """)

def ask_yes_no(question):
    #Ask a yes or no question
    response = None
    while response not in ("y" , "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    #Ask for a number withing a range
    response = None
    while response not in list(range(low,high)):
        response = int(input(question))
    return response


def pieces():
    #Determines who goes first

    go_first = ask_yes_no("Do you want to go first? (y/n)")

    if go_first == 'y':
        print("\nThen take the first move. You will need it.")
        human = X
        computer = O

    else:
        print("\nYou are brave! I'll go first.")
        computer = X
        human = O

    return computer, human

def new_board():
    #Create a new empty board

    board = []

    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    #Display board on screen

    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t","__________")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t","__________")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    #If an empty square is found, that is a legal move, otherwise not a legal move
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):

    WAYS_TO_WIN = ( (0,1,2), (3,4,5), (6,7,8),
                    (0,3,6), (1,4,7), (2,5,8),
                    (0,4,8), (2,4,6))

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
        move = ask_number("Where will you move? (0-8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("That square is already occupied, foolish human. Choose another.\n")
        print("Cool.")
    return move


def computer_move(board, computer, human):
    board = board[:]

    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("I shall take square number ", end=' ')

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
    if turn == "X":
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie. \n")

    if the_winner == computer:
        print("I triumph once again. It proves that computers are superior to humans!")
    elif the_winner == human:
        print("No, no! It cannot be. Somehow you tricked me, human! \n"\
              "But never again. I, the computer, so swears it.")
    elif the_winner == TIE:
        print("Lucky Human. You managed to tie me. Go celebrate for this is the best you will ever achieve.")

def main():
    display_instructions()
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
        if the_winner == computer or human:
            congrat_winner(the_winner, computer, human)

#START

main()
input("Press enter to exit")
        

    
