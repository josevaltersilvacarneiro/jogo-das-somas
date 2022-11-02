class Player:

    """
        This class defines all the actions and features of the player
    """

    def __init__(self, name : str):

        self._NAME : str = name
        self._score : int = 0

    # public

    @property
    def name(self) -> str:

        return self._NAME

    @property
    def score(self) -> int:

        return self._score

    @score.setter
    def score(self, points : int) -> None:

        self._score += points
