from constraint import BinaryConstraint


class Arc:

    def __init__(self, head, tail, const: BinaryConstraint):
        self.__head = head
        self.__tail = tail
        self.__cons = const

    def make_me_consistent(self, me_node):
        """ Makes head or tail arc consistent with respect to the other. """
        if me_node == self.__head:
            other_node = self.__tail
        elif me_node == self.__tail:
            other_node = self.__head


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
