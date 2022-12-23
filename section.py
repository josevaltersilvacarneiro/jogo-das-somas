from random import sample

from house import House

class Section:

    """
        This class creates a new type of data. The Section
        type is a tuple of unrepeated random elements.
    """
   
    def __init__(self, length : int):

        self._section : list = [
                    House(value) for value in sample(range(1, length + 1), length)
                ];

    def __getitem__(self, index) -> int:
        return self._section[index];

    @property
    def free(self) -> bool:

        for house in self._section:
            if house.status is False:
                return True;

        return False;

    def index(self, value : int) -> int:

        for i, house in enumerate(self._section):
            if house.value == value:
                return i;

        return -1;

if __name__ == '__main__':

    # Testing the class

    # Available methods using dir

    print(dir(Section))

    for i in range(1, 101):

        # Initializing the Section class

        init = Section(i)

        # Number of input, object repr, methods
        print(i, init, init[0].value ) # The other methods are handled for the tuple type

        # Errors

        # The length must not be less than 0
        # Output: raise ValueError('Sample larger than population or is negative')

        # If you call the method show and pass as parameter a type other than integer, you'll get a error
        # Examples: object.show(None), object.show(5.2)
        # Output: TypeError: '<' not supported between instances of 'NoneType' and 'int'
        # Output: TypeError: tuple indices must be integers or slices, not float
