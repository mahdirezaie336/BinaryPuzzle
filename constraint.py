class UnaryConstraint:

    def __init__(self, const_func):
        self.__const_func = const_func

    def satisfies(self, cell):
        return self.__const_func(cell)


class BinaryConstraint:

    def __init__(self, const_func):
        self.__const_func = const_func

    def satisfies(self, cell, cell2, node1, node2):
        return self.__const_func(cell, cell2, node1, node2)
