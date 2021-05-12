import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


class Tree:

    def __init__(self, is_mine, size):
        self.is_mine = is_mine
        self.size = size


class Cell:

    def __init__(self, index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5):
        self.index = index
        self.richness = richness
        self.neighbours_indexes = [neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5]
        self.tree = None

    def update_tree(self, tree):
        self.tree = tree


class Board:

    def __init__(self):
        self.cells = []
        self.day = None
        self.nutrients = None
        self.player_sun = None
        self.player_score = None
        self.opp_sun = None
        self.opp_score = None

    def add_cell(self, cell):
        self.cells.append(cell)

    def get_cell(self, cell_index):
        for c in self.cells:
            if c.index == cell_index:
                return c

    def complete_best_tree(self):
        best_score = 0
        best_cell_index = None
        for c in self.cells:
            if c.tree is not None:
                if c.tree.size == 3 and c.tree.is_mine:
                    score = board.nutrients + c.richness
                    if score > best_score:
                        best_score = score
                        best_cell_index = c.index

        print("COMPLETE {}".format(best_cell_index))
        self.get_cell(best_cell_index).update_tree(None)


board = Board()

number_of_cells = int(input())  # 37
for i in range(number_of_cells):
    # index: 0 is the center cell, the next cells spiral outwards
    # richness: 0 if the cell is unusable, 1-3 for usable cells
    # neigh_0: the index of the neighbouring cell for each direction
    idx, r, n0, n1, n2, n3, n4, n5 = [int(j) for j in input().split()]
    board.add_cell(Cell(idx, r, n0, n1, n2, n3, n4, n5))

# game loop
while True:
    board.day = int(input())  # the game lasts 24 days: 0-23
    board.nutrients = int(input())  # the base score you gain from the next COMPLETE action
    # sun: your sun points
    # score: your current score
    board.player_sun, board.player_score = [int(i) for i in input().split()]
    inputs = input().split()
    board.opp_sun = int(inputs[0])  # opponent's sun points
    board.opp_score = int(inputs[1])  # opponent's score
    opp_is_waiting = inputs[2] != "0"  # whether your opponent is asleep until the next day
    number_of_trees = int(input())  # the current amount of trees
    for i in range(number_of_trees):
        inputs = input().split()
        c_index = int(inputs[0])  # location of this tree
        tree_size = int(inputs[1])  # size of this tree: 0-3
        propietary = inputs[2] != "0"  # 1 if this is your tree
        is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
        board.get_cell(c_index).update_tree(Tree(propietary, tree_size))

    number_of_possible_actions = int(input())  # all legal actions
    for i in range(number_of_possible_actions):
        possible_action = input()  # try printing something from here to start with

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # GROW cellIdx | SEED sourceIdx targetIdx | COMPLETE cellIdx | WAIT <message>
    # print("WAIT")

    board.complete_best_tree()
