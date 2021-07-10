from cell import Cell
from constraint import UnaryConstraint, BinaryConstraint


class Node:

    __arcs: list

    def __init__(self, identity: tuple[str, int], cell_length):
        self.__arcs = []
        self.__id = identity
        self.__possible_cells = []
        self.__cell_length = cell_length

        self.init_possible_cells()

    def connect_to_another_node(self, other: 'Node', arc):
        self.__arcs.append(arc)
        other.__arcs.append(arc)

    def make_arc_consistent_to_all(self):
        """ Makes this node arc consistent with respect to all adjacent nodes. """
        for arc in self.__arcs:
            arc.make_me_consistent(self)

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

    def get_possible_cells(self):
        return self.__possible_cells

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.__id == other.__id

    def __hash__(self):
        return hash(self.__id)

    def __str__(self):
        return str(self.__id)

    def __repr__(self):
        return str(self.__id)


class Arc:

    def __init__(self, head: Node, tail: Node, const: BinaryConstraint):
        self.__head = head
        self.__tail = tail
        self.__cons = const                 # Head must be always first argument in binary constraint

    def make_me_consistent(self, me_node: Node):
        """ Makes head or tail arc consistent with respect to the other. """
        if me_node != self.__head and me_node != self.__tail:
            return

        other_node = self.get_other_side(me_node)
        cells = me_node.get_possible_cells()
        to_remove = []
        for cell in cells:
            found = False
            for other_cell in other_node.get_possible_cells():
                if self.__cons.satisfies(cell, other_cell):
                    found = True
                    break
            if not found:
                to_remove.append(cell)

        for cell in to_remove:
            cells.remove(cell)

    def get_other_side(self, node):
        """ Returns the node on others side of arc. """
        if node == self.__head:
            return self.__tail
        if node == self.__tail:
            return self.__head
        return None

    def get_constraint(self):
        """ Returns the constraint function. """
        return self.__cons

    def __str__(self):
        return str(self.__head) + ' -> ' + str(self.__tail)
