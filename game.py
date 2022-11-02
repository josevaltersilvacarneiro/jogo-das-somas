import sys

from display import Display
from board import Board
from player import Player

class Game:

    """
        This is main class of the game
    """

    def __init__(self):
        
        self.__DIMENSION : int = self.__get_dimension()
        self.__LENGTH : int = self.__DIMENSION ** 2

        self.__players : list = list()
        self.__AMOUNT_PLAYERS : int = self.__get_players()

        self.__quit : bool = False
        self.__next_player : int = 0
        
        self.__SUM_ROWS : list = list()
        self.__SUM_COLUMNS : list = [ 0 for i in range(self.__LENGTH) ]
        self.__SUM_DIAGONAL : int = 0
        self.__diagonal : bool = True


        self.__display : Display = Display(self.__LENGTH)
        self.__BOARD : Board = Board(self.__LENGTH)

        self.__sum_rows_columns_diagonal()

    @property
    def quit(self) -> bool:

        return self.__quit

    # private

    def get_digit(self, message : str) -> int:

        # As long as the variable digit isn't a digit, run

        while ( not ( digit := input(message) ).isdigit() ): pass

        return int(digit)

    def __convert(self, row_or_section : int, column_or_number_index : int) -> tuple:

        # This method converts row and column pair to section and number index pair and vice versa

        inv_rs = ( row_or_section // self.__DIMENSION ) * self.__DIMENSION + column_or_number_index // self.__DIMENSION
        inv_ci = ( row_or_section  % self.__DIMENSION ) * self.__DIMENSION + column_or_number_index  % self.__DIMENSION

        return inv_rs, inv_ci

    def __sum_rows_columns_diagonal(self) -> None:
        
        for i in range(self.__LENGTH):
            temp_i = 0
            for j in range(self.__LENGTH):

                section, number_index = self.__convert(i, j)

                number = self.__BOARD[section][number_index]

                self.__SUM_COLUMNS[j] += number
                temp_i += number
                if i == j: self.__SUM_DIAGONAL += number

            self.__SUM_ROWS.append(temp_i)

        self.__SUM_DIAGONAL = self.__SUM_DIAGONAL << 1 # double ;)

    # ++ section

    def _section_is_free(self, section : int) -> bool:
        
        # 0 => False ### The section is full
        # 1 => True  ### The section isn't full

        count = self.__LENGTH # It's necessary because going to decremented

        while ( count := count - 1 ) >= 0:

            row, column = self.__convert(section, count)

            if self.__display[row][column] is False: return True

        return False # If section has elements, so there is at least one free element

    def _number_is_free_on_section(self, number_index : int, section : int) -> bool:
        
        # 0 => False ### The number isn't free
        # 1 => True  ### Yes, the number is free

        row, column = self.__convert(section, number_index)

        return self.__display[row][column] is False

    def _number_index_on_section(self, number : int, section : int) -> bool:
        
        # This method returns the index's number on section number

        return self.__BOARD[section].index(number) # Exception tratment is desnecessary

    # -- section

    # + game

    def __game_over(self) -> int:

        # 0 => False ### There wasn't a win
        # 1 => True  ### There was a win

        # To win, the player must score more than the penultimate score plus the free points

        free_points = 0 # Sum of the points that nobody won; that is, points of the free positions in board

        for i in range(self.__LENGTH):

            if self.__display.row_is_free(i):
                free_points += self.__SUM_ROWS[i]

            if self.__display.column_is_free(i):
                free_points += self.__SUM_COLUMNS[i]

        if self.__display.diagonal_is_free():
            free_points += self.__SUM_DIAGONAL

        # It gets the score of each player and storages in players_score
        players_score = [ player.score for player in self.__players ]

        max_score = max(players_score); players_score.remove(max_score); penultimate_score = max(players_score)

        sum_of_scores = penultimate_score + free_points

        return sum_of_scores < max_score or free_points == 0

    def __get_dimension(self) -> int:

        while ( dimension := self.get_digit('Enter the dimension of the board, please: ') ) < 2:

            print('The minimum dimension of the board is 2', file=sys.stderr)

        return dimension

    def __get_players(self) -> int:

        while not 1 < ( amount_players := self.get_digit('Amount of players: ') ) <= self.__LENGTH:

            message = f'The minimum and maximum amount players are 2 and {self.__LENGTH} respectively'
            print(message, file=sys.stderr)

        for i in range(amount_players): 

            player_name = input('Name of the {}º player: '.format(i + 1)).title() # Get the name

            self.__players.append(
                        Player(player_name) # New player object
                    )

        return amount_players

    def __get_section_number(self) -> int:
        
        while True:

            section_number = self.get_digit(
                        f'Choose section number from 1 to {self.__LENGTH}, {self.__players[self.__next_player].name}: '
                            )

            if (
                    not 0 <= ( section_number := section_number - 1 ) < self.__LENGTH or
                    not self._section_is_free(section_number)
                ): continue

            return section_number

    def __get_number_on_section(self, section_number : int) -> int:

        while True:
            
            number = self.get_digit('Choose a free number: ')

            if (
                    not 0 < number <= self.__LENGTH or
                    not self._number_is_free_on_section(
                        ( number_index := self._number_index_on_section(number, section_number) ),
                        section_number
                    )
                ): continue

            return number_index

    # public 

    def show(self) -> None:
        
        print('==' * 30)

        for value in self.__SUM_COLUMNS:
            print('{:03}|'.format(value), end='') # columns
        else:
            print()

        for row_i in range(self.__LENGTH):
            for column_i, value in enumerate(self.__display[row_i]):

                section, number_index = self.__convert(row_i, column_i)

                print('{:03}|'.format(self.__BOARD[section][number_index]), end='') if value else print('XXX|', end='')

            print('{:03}'.format(self.__SUM_ROWS[row_i])) # rows
        else:
            print()

        #########################################
        # Reversed sort algorithm

        players = self.__players[:]
        sort_players = list()

        while players: # If players isn't empty, run
            
            highest_scoring_player = players[0]
            for player in players[1:]:

                if player.score > highest_scoring_player.score:
                    highest_scoring_player = player

            sort_players.append(highest_scoring_player)
            players.remove(highest_scoring_player)

        # End of reversed sort algorithm
        #########################################
        
        for player in sort_players:
            print('{}\t\t{:05}'.format(player.name, player.score))

        print('==' * 30)

    def play(self) -> None:
        
        # The player chooses the section and number pair that has not been selected yet

        # Section number; that is, the index of the number that was chosen by player
        section_number = self.__get_section_number()

        # Number index; that is, the index of the number that was chosen by player
        number_index = self.__get_number_on_section(section_number)

        # Conversion ;)
        row, column = self.__convert(section_number, number_index)

        # It marks the position on attribute called display as chosen
        self.__display[row][column] = True

        ##########################################
        # It makes the calculus for getting score

        # Row
        if not self.__display.row_is_free(row):

            self.__players[self.__next_player].score = self.__SUM_ROWS[row]

        # Column
        if not self.__display.column_is_free(column):

            self.__players[self.__next_player].score = self.__SUM_COLUMNS[column]

        # Diagonal
        if not self.__display.diagonal_is_free() and self.__diagonal:

            self.__players[self.__next_player].score = self.__SUM_DIAGONAL
            self.__diagonal = False

        # End of calculus for getting score
        #########################################

        # The position on attribute called display always was chosen and added at the score of the player

        # Did someone win or game over ?
        self.__quit = self.__game_over()

        # It defines the next player to play
        self.__next_player += 1; self.__next_player %= self.__AMOUNT_PLAYERS
