class Display:

    """
        This is the display: a class that storages a list with length boolean values
    """

    def __init__(self, length : int) -> None:
        
        self._index : int = -1

        self._LENGTH : int = length
        
        self._display = [
                    [ False for j in range(self._LENGTH) ] for i in range(self._LENGTH)
                ]

    def __len__(self) -> int:

        return self._display.__len__()

    def __getitem__(self, index) -> int:
        
        return self._display.__getitem__(index)

    def __setitem__(self, index, value) -> None:

        self._display._setitem__(index, value)
    
    def _is_free(self, typee : int = 2, index = None) -> bool:

        #   typee [
        #           0 => row
        #           1 => column
        #           2 => diagonal
        #       [
        #
        #   index of the row or column

        count = self._LENGTH

        while ( count := count - 1 ) >= 0:

            if typee == 0:
                value = self.__getitem__(index).__getitem__(count)
            elif typee == 1:
                value = self.__getitem__(count).__getitem__(index)
            else:
                value = self.__getitem__(count).__getitem__(count)

            if value is False:
                return True

        return False

    # public

    def row_is_free(self, row : int) -> bool:

        # 0 => False ### The row isn't free
        # 1 => True  ### Yes, the row is free

        return self._is_free(0, row)

    def column_is_free(self, column : int) -> bool:

        # 0 => False ### The column isn't free
        # 1 => True  ### Yes, the column is free

        return self._is_free(1, column)

    def diagonal_is_free(self) -> bool:

        # 0 => False ### The diagonal isn't free
        # 1 => True  ### Yes, the diagonal is free

        return self._is_free()
