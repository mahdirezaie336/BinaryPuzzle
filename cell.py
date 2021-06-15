class Cell:

    def __init__(self, value: str):
        self.__value = value

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return False
        return other.__value == self.__value


