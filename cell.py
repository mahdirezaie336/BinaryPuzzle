class Cell:

    def __init__(self, value: str):
        self.__value = value

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return False
        return other.__value == self.__value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self.__value

    def fits_on_mask(self, mask: str):
        """ Checks a mask with this object. A mask fits on this if .... """
        if len(mask) != len(self.__value):
            return False
        for i, char in enumerate(mask):
            if char in ['0', '1'] and char != self.__value[i]:
                return False
        return True

    def count_substring(self, sub_string: str):
        return self.__value.count(sub_string)

