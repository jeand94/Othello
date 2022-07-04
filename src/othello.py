


from constaints import NONE,WHITE,BLACK
from board import Board
from minmax import MinMax
# Game Rules

# Black always has the first move

# Each Move is valid if the opponents
# chip lies between the players chip and
# the move position. All chips in between
# change to the players chip color. Can
# be multi zoned such as a horizontal and
# vertical connection.

# If you can't outflank and flip at least
# one opposing disc, you must pass your turn.
# However, if a move is available to you, you
# can't forfeit your turn.

# Once a disc has been placed on a square, it can
# never be moved to another square later in the game.

# Valid moves are from the placed chip to the next
# found player chip. All chip between those points
# will be flipped



class Othello:
    board = Board()
    computer = MinMax()
    computer_active = False

    # Will make the move
    def make_move(self,position,user_chip_color,make_move):
        # Must Verifiy if a skip is present. Could Evaluate before
        # user even tries to work the problem.
        return self.board.move(position,user_chip_color,make_move)

    # Gets and returns the score for the black chip
    def get_black_chip_score(self):
        return self.board.black_chip_score

    # Makes the computer acitive and sets the computer
    # chip color
    def make_computer_active(self,color):
        self.computer.set_computer_color(color)
        self.computer_active = True

    # Gets the white chip color
    def get_white_chip_score(self):
        return self.board.white_chip_score

    # Get the current game board
    def get_board(self):
        return self.board

    # Gets the move the Game engine wants
    # to make
    def get_computer_move(self,board):
        # Automatically a skip if computer cant make move
        return self.make_move(computer.find_move(board),computer.color,True)

    # Checks if the game is over
    def is_game_over(self):
        # Both Players dont have a move left
