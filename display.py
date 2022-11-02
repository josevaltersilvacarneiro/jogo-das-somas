class Display:

    """
        This is the display: a class that storages a list with length boolean values
    """

    def __init__(self, length : int) -> None:
        
        self.__index : int = -1

        self.__LENGTH : int = length
        
        self.__display = [
                    [ False for j in range(self.__LENGTH) ] for i in range(self.__LENGTH)
                ]

    def __len__(self) -> int:

        return self.__display.__len__()

    def __getitem__(self, index) -> int:
        
        return self.__display.__getitem__(index)

    def __setitem__(self, index, value) -> None:

        self.__display.__setitem__(index, value)

    def __iter__(self):
        
        return self

    def __next__(self) -> int:

        if self.__index == self.__len__() - 1:
            self.__index = -1

            return StopIteration

        self.__index += 1

        return self.__getitem__(self.__index)

    def __is_free(self, typee : int = 2, index = None) -> bool:

        #   typee [
        #           0 => row
        #           1 => column
        #           2 => diagonal
        #       [
        #
        #   index of the row or column

        count = self.__LENGTH

        while ( count := count - 1 ) >= 0:

            if typee == 0: value = self.__getitem__(index).__getitem__(count) # equal to self.__getitem__(index)[count]
            elif typee == 1: value = self.__getitem__(count).__getitem__(index)
            else: value = self.__getitem__(count).__getitem__(count)

            if value is False: return True

        return False

    # public

    def row_is_free(self, row : int) -> bool:

        # 0 => False ### The row isn't free
        # 1 => True  ### Yes, the row is free

        return self.__is_free(0, row)

    def column_is_free(self, column : int) -> bool:

        # 0 => False ### The column isn't free
        # 1 => True  ### Yes, the column is free

        return self.__is_free(1, column)

    def diagonal_is_free(self) -> bool:

        # 0 => False ### The diagonal isn't free
        # 1 => True  ### Yes, the diagonal is free

        return self.__is_free()
