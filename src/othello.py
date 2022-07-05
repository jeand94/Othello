from constaints import NONE,WHITE,BLACK
from game import Game
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
    game = Game()
    computer = MinMax()

    # Will make the move
    def make_move(self,position,user_chip_color,make_move):
        # Must Verifiy if a skip is present. Could Evaluate before
        # user even tries to work the problem.
        return self.game.move(position,user_chip_color,make_move)

    # Gets and returns the score for the black chip
    def get_black_chip_score(self):
        return self.game.black_chip_score

    # Makes the computer acitive and sets the computer
    # chip color
    def make_computer_active(self,color):
        self.computer.set_computer_color(color,5)

    # Gets the white chip color
    def get_white_chip_score(self):
        return self.game.white_chip_score

    # Get the current game board
    def get_game_board(self):
        return self.game

    # Gets the move the Game engine wants
    # to make
    def make_computer_move(self,color):
        # Automatically a skip if computer cant make move
        return self.make_move(self.computer.find_move(self.game),color,True)

    # Checks if the game is over
    def is_game_over(self):
        return False
        # Both Players dont have a move left
