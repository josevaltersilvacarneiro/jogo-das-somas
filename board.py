from section import Section

class Board:

    """
        This class creates the board of the game: a array of sections
    """

    def __init__(self, length : int) -> None:

        self._board = [ Section(length) for i in range(length) ]

    def __getitem__(self, index : int) -> Section:

        return self._board.__getitem__(index)
