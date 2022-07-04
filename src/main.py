
import time
from othello import Othello
from position import Position
from constaints import NONE,WHITE,BLACK




print ("Welcome to my Othello game. LETS PLAY!!\n")
print ("A: Multiplayer mode")
print ("B: Single player mode")
option = str(input("Enter your option >> "))
user_chip = ''
current_player = BLACK
if option == 'B'or option == 'b':
    print("Please enter your color")
    print("W: white")
    print("B: black")
    print("Note: Black gets first play!!!")
    user_chip = str(input("Enter your option >> "))
elif option != 'A' and  option != 'a' :
    print("Wrong option was entered. Game will now exit")
    exit()




#While loop for game
game_over = False
newgame = Othello()
while not game_over :

    print(newgame.get_board())

    if current_player == WHITE:
        print("White: Please select your move position")
    elif current_player == BLACK:
        print("Black: Please select your move position")

    row = int(input("Enter your row >> "))
    column = int(input("Enter your column: "))

    move_complete = newgame.make_move(Position(row,column),current_player,True)

    if not move_complete:
        print("\nThat was an invalid move. Please try again")

    if move_complete:
        if current_player == BLACK:
            current_player = WHITE
        else :
            current_player = BLACK
    #game_over = Othello.is_game_over()

#printBoard(newgame.board)






#newgame.isValidMove(1,row,column)
#sum=newgame.makeMove(1,row,column)
print("made it")
exit()
