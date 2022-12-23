import sys

from _utils import convert
from board import Board

class Display:
    """This class is responsible for presenting
    the game.
    
    """

    def __init__(self) -> None:
        
        self._DIMENSION : int   = self._get_dimension();
        self._LENGTH    : int   = pow(self._DIMENSION, 2);
        self._BOARD     : Board = Board(self._LENGTH);
        self._quit      : bool  = False;
        
    def __str__(self):
        
        representation = '';
        representation += ('=' * 30) + '\n';
        representation += str(self._BOARD);
        representation += ('=' * 30) + '\n';

        return representation;

    @property
    def quit(self) -> bool:
        
        for section in self._BOARD:
            for house in section:
                if house.status is False:
                    return False;

        self.quit = True;

        return self._quit;

    @quit.setter
    def quit(self, new_status : bool) -> None:
        self._quit = new_status;

    # private

    def _get_amount(self, message : str) -> int:

        while not ( amount := input(message) ).isdecimal():
            print(f'{amount} isn\'t a valid number', file=sys.stderr);

        return int(amount);

    def _get_dimension(self) -> int:

        while ( dimension := self._get_amount('Type the dimension of the board, please: ') ) < 2:
            print('The minimum dimension of the board is 2', file=sys.stderr);

        return dimension;

    def _get_section(self) -> int:
        
        while True:

            section : int = self._get_amount('Type the section: ') - 1;

            if (
                    0 <= section < self._LENGTH and
                    self._BOARD[section].free
                ): return section;

    def _get_house(self, section : int) -> int:
        
        while True:

            house : int = self._get_amount('Type the house: ');

            if 0 < house <= self._LENGTH:
                house_index = self._BOARD[section].index(house);
            else:
                continue;

            if self._BOARD[section][house_index].status is False:
                self._BOARD[section][house_index].status = True;
                return house_index;

    # public

    def get_players(self) -> list:
        
        players : list = [];

        while not 1 < (number_of_players := self._get_amount('Number of players: ')) <= self._LENGTH:

            message = f'The minimum and maximum number of players is 2 and {self._LENGTH}';
            print(message, file=sys.stderr);
        
        for i in range(number_of_players):

            player_name = input(f'Name of the {i+1}º player: ');
            players.append(player_name);

        return players;

    def get_option(self) -> tuple:

        section : int = self._get_section();
        house   : int = self._get_house(section);

        return convert(section, house, self._DIMENSION);

    def is_row_free(self, row : int) -> bool:
        return self._BOARD.is_row_free(row);

    def is_column_free(self, column : int) -> bool:
        return self._BOARD.is_column_free(column);

    def is_diagonal_free(self) -> bool:
        return self._BOARD.is_diagonal_free()

    def rows_sum(self, row : int) -> int:
        return self._BOARD.rows_sum[row];

    def columns_sum(self, column : int) -> int:
        return self._BOARD.columns_sum[column];

    def diagonal_sum(self) -> int:
        return self._BOARD.diagonal_sum
