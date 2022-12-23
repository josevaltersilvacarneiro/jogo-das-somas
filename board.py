from _utils import convert
from section import Section

class Board:
    """This class creates the board of the game:
    a list of sections. After being instantiated
    the values cannot be changed; but the main
    program can access them. For example:

    new_board = Board(2);
    section_one = new_board[1];

    To print the board on screen:
    print(new_board);
    
    """

    def __init__(self, length : int) -> None:

        self._DIMENSION : int  = int(length ** 0.5);
        self._LENGTH    : int  = pow(self._DIMENSION, 2);
        self._BOARD     : list = [
                    Section(self._LENGTH) for i in range(self._LENGTH)
                ];

        self._rows_sum     : list = [0 for i in range(self._LENGTH)];
        self._columns_sum  : list = [0 for i in range(self._LENGTH)];
        self._diagonal_sum : int  = 0;

        self._find_the_sums();

    def __str__(self) -> str:

        board : str = '';

        for value in self.columns_sum:
            board += f'{value:03}|';
        else:
            board += '\n';

        for row in range(self._LENGTH):
            for column in range(self._LENGTH):

                section, house = convert(row, column, self._DIMENSION);
                board += f'{self._BOARD[section][house].value:03}|' if self._BOARD[section][house].status else 'XXX|';
            
            board += str(self.rows_sum[row]) + '\n';

        return board;

    def __getitem__(self, index : int) -> Section:
        return self._BOARD[index];

    @property
    def rows_sum(self) -> list:
        return self._rows_sum;

    @property
    def columns_sum(self) -> list:
        return self._columns_sum;

    @property
    def diagonal_sum(self) -> int:
        return self._diagonal_sum;

    @diagonal_sum.setter
    def diagonal_sum(self, value) -> None:
        self._diagonal_sum = value << 1;

    def _find_the_sums(self):
        """This method stores the sum of each row and column
        in rows_sum and columns_sum attributes respectively.
        Furthermore, it finds the sum of the main diagonal.
        To do this, it first needs to convert the row and
        column pair to section and house to get the corres-
        ponding value. This is done with the convert func-
        tion.

        """

        for row in range(self._LENGTH):
            for column in range(self._LENGTH):

                section, house            = convert(row, column, self._DIMENSION);
                number                    = self._BOARD[section][house].value;

                self.columns_sum[column] += number;
                self.rows_sum[row]       += number;

                if row == column:
                    self.diagonal_sum    += number;

    def is_row_free(self, row : int) -> bool:
        
        for column in range(self._LENGTH):
            
            section, house = convert(row, column, self._DIMENSION);

            if self._BOARD[section][house].status is False:
                return True;

        return False;

    def is_column_free(self, column : int) -> bool:

        for row in range(self._LENGTH):

            section, house = convert(row, column, self._DIMENSION);

            if self._BOARD[section][house].status is False:
                return True;

        return False;

    def is_diagonal_free(self) -> bool:

        for i in range(self._LENGTH):

            section, house = convert(i, i, self._DIMENSION);

            if self._BOARD[section][house].status is False:
                return True;

        return False;

#-----------------------------------------------------------------#
#---------------------------- Tests ------------------------------#

if __name__ == '__main__':

    # Testing the Board class

    # Available methods using dir

    print(dir(Board))

    for i in [4, 9]:

        # Initializing the Board class

        init = Board(i)

        # Number of input, object repr, methods
        print(i, init, sep='\n')

        # Errors

        # If the method __getitem__ receives as parameter a index greater or smaller 
        # than the length of board object, it returns a error
        # Output: IndexError: list index out of range
