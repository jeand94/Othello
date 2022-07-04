from node import Node
from constaints import NONE,WHITE,BLACK
import copy

class MinMax :
    color = "O"
    opponent_color = "O"
    depth = 1
    root_node = Node()
    infinity = 1000000

    def find_move(self,board):
        self.root_board = copy.deepcopy(board)
        self.alpha_beta_algorithm()

    def alpha_beta_algorithm(self):
        best_val = –self.infinity
        beta = self.infinity
        best_node = Node()
        level = 1
        # Get a list of possible moves
        children = self.root_node.nodes
        # loop through those moves
        # Make the move
        # append to the Node child
        for child in children:
            value = self.min_value(child, best_value, beta, level)
            if value > best_value
                best_value = value
                best_node = child

        return best_node.last_move_made()

        def alpha_beta_search(self, node):

    def min_alpha_beta(self,node,alpha,beta,level):
        level = level + 1

        if(level == self.depth):
            return 0
        if bool(node.nodes):
            # return this node_evaluation
            return self.getUtility(node)

        value = infinity

        # Need to make sure children are created.
        # More Information can be
        children = node.nodes

        for child in children:
            value = min(value, self.min_alpha_beta(child, alpha, beta,level))
            if value <= alpha:
                return value
            beta = min(beta, value)

        return value

    def max_alpha_beta(self,node,alpha,beta,level):
        level = level + 1

        if(level == self.depth):
            return 0
        if bool(node.nodes):
            # return this node_evaluation
            return self.getUtility(node)

        value = -self.infinity
        children = node.nodes

        for child in children:
            value = max(value, self.min_value(node, alpha, beta,level))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    def set_computer_color(self,color,depth):
        self.color = color
        self.depth = depth

        if(color == WHITE):
            self.opponent_color = BLACK
        else :
            self.opponent_color = WHITE

    def node_evaluation(self,node):
        print("Hello World")
        # Evaluate by player Score
        # Evaluate by Amount of items in edges

    def populate_children_nodes(self,node):
        # Get potention_moves
        # I need the board with the changes
        # I need the move that was made
        # I need the color of the player that moved
