from functools import total_ordering

@total_ordering
class Player:
    """When instantiating a new Player object,
    the player's name must be passed as argu-
    ment. For example:

    new_player = Player('John');

    The name and score attributes are publicly
    available. To access them, use the methods
    below:

    new_player_name  = new_player.name;
    new_player_score = new_player.score;

    The player's score can be changed. However,
    the value will be incremented, i.e. it's
    not possible to decrease it. See below:

    print(new_player.score); # 5
    new_player.score += 5;
    print(new_player.score); # 10
    
    """

    def __init__(self, name : str):

        self._NAME  : str = name;
        self._score : int = 0;

    def __eq__(self, player : object) -> bool:
        return self.score == player.score;

    def __lt__(self, player : object) -> bool:
        return self.score < player.score;

    # public

    @property
    def name(self) -> str:
        return self._NAME;

    @property
    def score(self) -> int:
        return self._score;

    @score.setter
    def score(self, points : int) -> None:
        self._score = points;
