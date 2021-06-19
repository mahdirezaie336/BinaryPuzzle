from constraint import BinaryConstraint
from node import Node


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

    def get_other_side(self, node):
        """ Returns the others side node. """
        if node == self.__head:
            return self.__tail
        if node == self.__tail:
            return self.__head
        return None

    def get_constraint(self):
        """ Returns the constraint function. """
        return self.__cons
