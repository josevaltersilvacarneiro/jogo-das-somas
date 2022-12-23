from display import Display
from player import Player

class Game:
    """This is main class of the game

    """

    def __init__(self):
        
        self._display           : Display = Display();
        self._players           : list    = [
                    Player(name) for name in self._display.get_players()
                ];
        self._number_of_players : int     = len(self._players);
        self._next_player       : int     = 0;
        self._diagonal          : bool    = True;
        self._quit              : bool    = False;
        
    @property
    def quit(self) -> bool:
        return self._display.quit;

    @property
    def next_player(self) -> int:
        """To find out the next player to play, it
        increments the _next_player attribute by
        1. After that, it calculates the module in
        relation the number of players.

        """
        
        self._next_player += 1;
        self._next_player %= self._number_of_players;

        return self._players[self._next_player];

    # public 

    def show(self) -> None:
        
        print(self._display);

        for player in sorted(self._players, reverse=True):
            print('{}\t\t{:05}'.format(player.name, player.score))

    def play(self, player : Player) -> None:
        
        row, column = self._display.get_option();

        # Row
        if not self._display.is_row_free(row):
            player.score += self._display.rows_sum(row);

        # Column
        if not self._display.is_column_free(column):
            player.score += self._display.columns_sum(column);

        # Diagonal
        if not self._display.is_diagonal_free() and self._diagonal:
            player.score += self._display.diagonal_sum();
            self._diagonal = False
