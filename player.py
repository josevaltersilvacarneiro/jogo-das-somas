from functools import total_ordering

@total_ordering
class Player:

    """
        This class defines all the actions and features of the player
    """

    def __init__(self, name : str):

        self._NAME : str = name
        self._score : int = 0

    def __eq__(self, player : object) -> bool:
        return self._score == player.score

    def __lt__(self, player : object) -> bool:
        return self._score < player.score;

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
