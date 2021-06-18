class Arc:

    def __init__(self, head, tail, const):
        self.__head = head
        self.__tail = tail
        self.__cons = const

    def make_me_consistent(self, node):
        """ Makes head or tail arc consistent with respect to the other. """
        if node == self.__head:
            node.make_arc_consistent_to(self.__tail)
        elif node == self.__tail:
            node.make_arc_consistent_to(self.__head)
        pass

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
