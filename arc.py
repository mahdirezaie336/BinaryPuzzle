class Arc:

    def __init__(self, head, tail, const):
        self.__head = head
        self.__tail = tail
        self.__cons = const

    def make_me_consistent(self, node):
        """ Makes head or tail arc consistent with respect to the other. """
        if node == self.__head:
            node.make_arc_consistent_to()
        pass
