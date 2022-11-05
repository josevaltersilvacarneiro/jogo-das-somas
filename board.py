from section import Section

class Board:

    """
        This class creates the board of the game: a array of sections
    """

    def __init__(self, length : int) -> None:

        self._board = [ Section(length) for i in range(length) ]

    def __getitem__(self, index : int) -> Section:

        return self._board.__getitem__(index)

if __name__ == '__main__':

    # Testing the Board class

    # Available methods using dir

    print(dir(Board))

    for i in range(-100, 101):

        # Initializing the Board class

        init = Board(i)

        # Number of input, object repr, methods
        print(i, init)

        # Errors

        # If the method __getitem__ receives as parameter a index greater or smaller 
        # than the length of board object, it returns a error
        # Output: IndexError: list index out of range
