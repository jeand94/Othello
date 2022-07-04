


from constaints import NONE,WHITE,BLACK
from board import Board
# Game Rules

# Black always has the first move

# Each Move is valid if the opponents
# chip lies between the players chip and
# the move position. All chips in between
# change to the players chip Color. Can
# be multi zoned such as a horizontal and
# vertical connection.

# If you can't outflank and flip at least
# one opposing disc, you must pass your turn.
# However, if a move is available to you, you
# can't forfeit your turn.

# Once a disc has been placed on a square, it can
# never be moved to another square later in the game.

# When a player runs out of discs, but still has
# opportunities to outflank an opposing disc, then
# the opponent must give the player a disc to use.

# Each player takes 32 discs and chooses one colour
# to use throughout the game

# valid from the placed chip to the next found player chip.
# all chip between those points with be flipped

# Objects that will be included in this program
# User Interface class
# Othello Game class
# MinMax Class has moves class should be different will have a list of
# Board class that will handle the moves.

# an implementation that is better would be using a hash map.
# the key will be the board position. This can be an array Objects
# [0,0]. The value will be BLACK or WHITE, Witch will be constaints
# for 1,2. When a player wants to make a move you will get his selected
# postion ie [2,3]. You will then get a list of keys that have the player
# value. Then you check for keys that have the same slop. Then check if they
# are on the same path. If a you have multiple chips in path. Connect with the
# closest chip for the move. Update the hash table. Lookup should be O(1).

# This implementation will help with the minmax algorithm and making it
# operate much faster. With array boards we would have to have n^2 lookup
# per tree created by the minmax algorithm. Moves would take too long. Big O(n)
# with this implementation.

#psuedoCode for move
#User selects Move [2,3]
#Get a list Keys of the opposit player O(n)
#Check if the new move is by the oppisit player. Add this to lists
#Would be less work to just check following the slop given in the lists
#till we reach the user
#

# task create the user Interface
# create the minmax algorithm

class Othello:
    board = Board()

    def make_move(self,position,user_chip_color,make_move):
        return self.board.move(position,user_chip_color,make_move)

    def get_black_chip_score(self):
        return self.board.black_chip_score

    def get_white_chip_score(self):
        return self.board.white_chip_score

    def get_board(self):
        return self.board
