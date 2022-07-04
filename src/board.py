
from position import Position
from constaints import NONE,WHITE,BLACK



class Board:

    # Define Othello board using a dictionary
    # and a user defined key
    board = {
        # Row,Column
        Position(1,1): NONE,
        Position(1,2): NONE,
        Position(1,3): NONE,
        Position(1,4): NONE,
        Position(1,5): NONE,
        Position(1,6): NONE,
        Position(1,7): NONE,
        Position(1,8): NONE,
        Position(2,1): NONE,
        Position(2,2): NONE,
        Position(2,3): NONE,
        Position(2,4): NONE,
        Position(2,5): NONE,
        Position(2,6): NONE,
        Position(2,7): NONE,
        Position(2,8): NONE,
        Position(3,1): NONE,
        Position(3,2): NONE,
        Position(3,3): NONE,
        Position(3,4): NONE,
        Position(3,5): NONE,
        Position(3,6): NONE,
        Position(3,7): NONE,
        Position(3,8): NONE,
        Position(4,1): NONE,
        Position(4,2): NONE,
        Position(4,3): NONE,
        Position(4,4): WHITE,
        Position(4,5): BLACK,
        Position(4,6): NONE,
        Position(4,7): NONE,
        Position(4,8): NONE,
        Position(5,1): NONE,
        Position(5,2): NONE,
        Position(5,3): NONE,
        Position(5,4): BLACK,
        Position(5,5): WHITE,
        Position(5,6): NONE,
        Position(5,7): NONE,
        Position(5,8): NONE,
        Position(6,1): NONE,
        Position(6,2): NONE,
        Position(6,3): NONE,
        Position(6,4): NONE,
        Position(6,5): NONE,
        Position(6,6): NONE,
        Position(6,7): NONE,
        Position(6,8): NONE,
        Position(7,1): NONE,
        Position(7,2): NONE,
        Position(7,3): NONE,
        Position(7,4): NONE,
        Position(7,5): NONE,
        Position(7,6): NONE,
        Position(7,7): NONE,
        Position(7,8): NONE,
        Position(8,1): NONE,
        Position(8,2): NONE,
        Position(8,3): NONE,
        Position(8,4): NONE,
        Position(8,5): NONE,
        Position(8,6): NONE,
        Position(8,7): NONE,
        Position(8,8): NONE,
    }
    # Define a List of positions which
    # will be the edges of the white chips
    white_chip_edges = [
        Position(5,5),
        Position(4,4)
    ]

    # Define a List of positions which
    # will be the edges of the white chips
    black_chip_edges = [
        Position(4,5),
        Position(5,4)
    ]
    # When looking up or trying to find new Moves
    # look for NONE neighbors of the the opponent
    # that would generate a list of potential Moves
    # this keeps us from having to iterate through
    # the entire dictionary each time we are looking
    # for a move. 

    # Score of the black chip player
    black_chip_score = 2

    # Score of the white chip player
    white_chip_score = 2

    # Defining how this object will be printed
    # as string element. Here we create a table
    # board that will be used to play the game
    def __str__(self):
        itr = 1
        rows = [1, 2, 3, 4, 5, 6, 7, 8]
        output = ""
        output = output + "\n\n-0-  -1- -2- -3- -4- -5- -6- -7- -8-\n"
        for row in rows:
            output = output + (f"-{itr}- | " +
            f"{self.board.get(Position(row, 1 ))}" +
            f" | {self.board.get(Position(row, 2 ))}" +
            f" | {self.board.get(Position(row, 3 ))}" +
            f" | {self.board.get(Position(row, 4 ))}" +
            f" | {self.board.get(Position(row, 5 ))}" +
            f" | {self.board.get(Position(row, 6 ))}" +
            f" | {self.board.get(Position(row, 7 ))}" +
            f" | {self.board.get(Position(row, 8 ))}" +
             " |\n")

            itr = itr + 1

        output = output + (f"\n\nBlack player current score = {self.black_chip_score}")
        output = output + (f"\nWhite player current score = {self.white_chip_score}\n\n")

        return output

    # Function that will handle all of the moves
    def move(self,position,color,make_move):
        valid_moves = 0
        potential_moves = self.check_neighbors(position,color)

        for move in potential_moves:
            self.connect_chips(move, position, color)
            if(bool(move)):
                valid_moves = valid_moves + 1
                if make_move :
                    self.update_edge_cases(move,color,position)
                    self.flip_chips(move,color)
                    self.update_score(move,color)

        if valid_moves == 0:
            return False
        else:
            return True

    # Function that will change the color of the chips
    # passed to it
    def flip_chips(self,move,color):

        for position in move.keys():
            self.board.update({position:color})

    # Will get and return the opponenets chip color
    def get_opponent_color(self,color):
        opponent_color = NONE

        if color == BLACK:
            opponent_color = WHITE
        else :
            opponent_color = BLACK

        return opponent_color

    # Function that will look for valid Moves.
    # Will return an empty dictionary if nothing was
    # found. Else will return all of the positions
    # for the move
    def connect_chips(self, move, position, color):
        is_done = False
        row = 0
        column = 0
        row_factor = 0
        column_factor = 0

        opponent_color = self.get_opponent_color(color)


        for move_position in move.keys():
            if move.get(move_position) == opponent_color:
                row = move_position.row
                column = move_position.column

        row_factor = (position.row - row) * -1
        column_factor = (position.column - column) * -1

        while( not is_done):
            row =  row + row_factor
            column = column + column_factor

            if self.board.get(Position(row, column )) == opponent_color:
                move.update({Position(row, column):opponent_color})
            elif self.board.get(Position(row, column )) == color :
                is_done = True
                move.update({Position(row, column):color})
            elif row == 0 or column == 0 or self.board.get(Position(row, column )) == NONE :
                move.clear()
                is_done = True

    # This will update the score of each player
    def update_score(self,move,color):
        added_chips = len(move) - 2

        if color == BLACK:
            self.black_chip_score = self.black_chip_score + added_chips
            self.white_chip_score = self.white_chip_score - added_chips
        else:
            self.black_chip_score = self.black_chip_score - added_chips
            self.white_chip_score = self.white_chip_score + added_chips

    # This will update the edge chips for each colored chip
    def update_edge_cases(self,move,color,position):

        for move_position in move.keys():
            if color == WHITE and move_position == position:
                self.white_chip_edges.append(position)
            elif color == BLACK and move_position == position:
                self.black_chip_edges.append(position)
            elif color == WHITE and move_position in self.black_chip_edges:
                self.black_chip_edges.remove(move_position)
                self.white_chip_edges.append(move_position)
            elif color == BLACK and move_position in self.white_chip_edges:
                self.white_chip_edges.remove(move_position)
                self.black_chip_edges.append(move_position)

    # Checks to if there are any opponent chips near
    # the move position. Will return a list of All
    # neighbors.
    def check_neighbors(self,position,color):
        row = position.row
        column = position.column
        neighbors = [];
        positions = [[row + 1, column ],
                     [row - 1, column ],
                     [row, column + 1 ],
                     [row, column - 1 ],
                     [row + 1, column + 1 ],
                     [row + 1, column - 1 ],
                     [row - 1, column - 1 ],
                     [row - 1, column + 1 ]]

        opponent_color = self.get_opponent_color(color)

        for coordinates in positions:
            if self.board.get(Position(coordinates[0],coordinates[1])) == opponent_color:
                neighbors.append({
                    position: color,
                    Position(coordinates[0],coordinates[1]): opponent_color
                    }
                )

        return neighbors
