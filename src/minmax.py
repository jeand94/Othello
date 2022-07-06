from node import Node
from constaints import NONE,WHITE,BLACK, WEIGHTS
from game import Game
from position import Position

import copy

class MinMax :
    color = "O"
    opponent_color = "O"
    depth = 1
    root_node = Node()
    infinity = 1000000

    # Entry point for the minmax class
    # where initilize the root and call
    # the alpha beta prunnign algoritm
    def find_move(self,game):
        self.root_node = Node()
        self.root_node.nodes.clear()

        for key,value in game.board.items():
            self.root_node.game.board[copy.deepcopy(key)] = copy.deepcopy(value)

        self.root_node.game.white_chip_edges = copy.deepcopy(game.white_chip_edges)
        self.root_node.game.black_chip_edges = copy.deepcopy(game.black_chip_edges)
        self.root_node.game.black_chip_score = copy.deepcopy(game.black_chip_score)
        self.root_node.game.white_chip_score = copy.deepcopy(game.white_chip_score)

        return self.alpha_beta_algorithm()

    def alpha_beta_algorithm(self):
        best_value = self.infinity * -1
        beta = self.infinity
        best_node = Node()
        level = 1

        self.populate_children_nodes(self.root_node,self.color)
        children = self.root_node.nodes.copy()

        for child in children:
            value = self.min_alpha_beta(child, best_value, beta, level)
            if value > best_value:
                best_value = value
                self.copy_from_parent(best_node,child)

        return copy.deepcopy(best_node.last_move_made)

    # Min Aplha beta prunning function
    def min_alpha_beta(self,node,alpha,beta,level):
        level = level + 1
        if level == self.depth:
            return self.node_evaluation(node)

        value = self.infinity

        self.populate_children_nodes(node,self.opponent_color)

        children = copy.deepcopy(node.nodes)

        if(not bool(children)):
            return self.node_evaluation(node)
        for child in children:
            value = min(value, self.max_alpha_beta(child, alpha, beta,level))
            if value <= alpha:
                return value
            beta = min(beta, value)

        return value

    # Max aplha beta prunning section
    def max_alpha_beta(self,node,alpha,beta,level):
        level = level + 1

        if level == self.depth :
            return self.node_evaluation(node)

        value = self.infinity * -1

        self.populate_children_nodes(node,self.color)

        children = copy.deepcopy(node.nodes)

        if(bool(children)):
            return self.node_evaluation(node)

        for child in children:
            value = max(value, self.min_alpha_beta(node, alpha, beta,level))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    # Sets who the computer player is
    def set_computer_color(self,color,depth):
        self.color = color
        self.depth = depth

        if(color == WHITE):
            self.opponent_color = BLACK
        else :
            self.opponent_color = WHITE

    # This is the weight function for each game
    # board found in the tree
    def node_evaluation(self,node):
        black_chip_weight = 0
        white_chip_weight = 0
        weight = 0
        keys = node.game.board.keys()

        for key in keys:
            color = node.game.board[key]
            if color == BLACK :
                black_chip_weight += WEIGHTS[key]
            elif color == WHITE:
                white_chip_weight += WEIGHTS[key]

        if self.color == WHITE:
            weight = white_chip_weight - black_chip_weight
        else:
            weight = black_chip_weight - white_chip_weight

        return weight

    # Copies one node to another.
    def copy_from_parent(self,child_node,node):
        for key,value in node.game.board.items():
            child_node.game.board[copy.deepcopy(key)] = copy.deepcopy(value)

        child_node.game.white_chip_edges = copy.deepcopy(node.game.white_chip_edges)
        child_node.game.black_chip_edges = copy.deepcopy(node.game.black_chip_edges)
        child_node.game.black_chip_score = copy.deepcopy(node.game.black_chip_score)
        child_node.game.white_chip_score = copy.deepcopy(node.game.white_chip_score)
        child_node.last_move_made = copy.deepcopy(node.last_move_made)

    def populate_children_nodes(self,node,active_color):
        positions = node.game.find_moves(active_color)

        # if the positions list is
        # not empty
        if bool(positions):
            for position in positions:
                child_node = Node()
                self.copy_from_parent(child_node,node)
                child_node.game.move(position,active_color,True)
                child_node.last_move_made = copy.deepcopy(position)
                child_node.move_color = active_color
                node.nodes.append(child_node)
