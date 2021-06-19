from cell import Cell
from constraint import UnaryConstraint


class Node:

    __arcs: list

    def __init__(self, identity, cell_length):
        self.__arcs = []
        self.__id = identity
        self.__possible_cells = []
        self.__cell_length = cell_length

        self.init_possible_cells()

    def make_arc_consistent_to(self, node):
        """ Makes this node arc consistent with respect to another node. """
        pass

    def init_possible_cells(self):
        """ Initializes all possible cells. """
        for i in range(self.__cell_length):
            self.__possible_cells.append(Cell('{:b}'.format(i).zfill(self.__cell_length)))

    def apply_unary_constraint(self, const: UnaryConstraint):
        """ Removes cells which do not satisfy the unary constraint from possible cells. """
        to_remove = []
        for cell in self.__possible_cells:
            if not const.satisfies(cell):
                to_remove.append(cell)

        for cell in to_remove:
            self.__possible_cells.remove(cell)

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
