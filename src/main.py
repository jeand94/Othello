from othello import Othello
from position import Position
from constaints import NONE,WHITE,BLACK


user_chip = NONE
current_player = BLACK
game_over = False
game = Othello()

# Introduction
print ("Welcome to my Othello game. LETS PLAY!!\n")

# Getting the game option
print ("A: Multiplayer mode")
print ("B: Single player mode")
option = str(input("Enter your option >> "))

# Getting option if playing computer
if option == 'B'or option == 'b':
    print("Please enter your color")
    print("W: white")
    print("B: black")
    print("Note: Black gets first play!!!")
    user_chip = str(input("Enter your option >> "))
elif option != 'A' and  option != 'a' :
    # Error
    print("Wrong option was entered. Game will now exit")
    exit()

if user_chip == 'w' or user_chip == 'w':
    user_chip = WHITE
    game.make_computer_active(BLACK)
elif user_chip == 'b' or user_chip == 'b':
    user_chip = BLACK
    game.make_computer_active(WHITE)
else :
    print("Wrong option was entered. Game will now exit")
    exit()

# Main while loop for the game
while not game_over :

    print(game.get_game_board())

    if user_chip == NONE:
        if current_player == WHITE:
            print("White: Please select your move position")
        elif current_player == BLACK:
            print("Black: Please select your move position")

        row = int(input("Enter your row >> "))
        column = int(input("Enter your column: "))
        move_complete = game.make_move(Position(row,column),current_player,True)
    elif user_chip == current_player:
        print("Please enter your move position")
        row = int(input("Enter your row >> "))
        column = int(input("Enter your column: "))
        move_complete = game.make_move(Position(row,column),current_player,True)
    else:
        move_complete =  game.make_computer_move(current_player)

    if not move_complete:
        print("\nThat was an invalid move. Please try again")

    if move_complete:
        if current_player == BLACK:
            current_player = WHITE
        else :
            current_player = BLACK

    move_complete = False
exit()
