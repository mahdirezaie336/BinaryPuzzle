from cell import Cell


class Node:

    str_len = 4
    __arcs: list

    def __init__(self, identity):
        self.__arcs = []
        self.__id = identity
        self.__possible_cells = []

    def make_arc_consistent_to(self, node):
        """ Makes this node arc consistent with respect to another node. """
        pass

    def init_possible_cells(self):
        """ Initializes all possible cells. """
        for i in range(Node.str_len):
            self.__possible_cells.append(Cell('{:b}'.format(i).zfill(Node.str_len)))

    def apply_unary_constraint(self, const):
        """ Applies a unary constraint to all possible sets. """
        pass

    def apply_binary_constraint(self, const):
        """ Applies a binary constraint to all possible values.
            Makes the node arc consistent with respect to all possible nodes. """
        pass

    def apply_mask_filter(self, mask):
        """ Applies a filter by given mask on possible cells. """
        to_delete = []
        for cell in self.__possible_cells:
            if cell.fits_on_mask(mask):
                to_delete.append(cell)

        for cell in to_delete:
            self.__possible_cells.remove(cell)

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.__id == other.__id

    def __hash__(self):
        return hash(self.__id)
