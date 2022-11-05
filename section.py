from random import sample

class Section(tuple):

    """
        This class creates a new type of data. The Section
        type is a tuple of unrepeated random elements.
    """
   
    def __new__(self, length : int):

        return super().__new__(
                    Section,
                    sample(range(1, length + 1), length)
                )

    # Private

    def _not_contain(self, number : int) -> bool:

        return number not in self.__iter__()

    # Public

    def show(self, index : int) -> int:

        if -self.__len__() <= index < self.__len__():
            return self.__getitem__(index)
        
        return None

    def index(self, number : int, return_value = None) -> int:

        # Call this method like this: 
        # object.index(
        #               the number that you want to know the index, 
        #               [ the optional return value if number doens't in object [
        #           )

        if self._not_contain(number):
            return return_value
        
        return super().index(number)


if __name__ == '__main__':

    # Testing the class

    # Available methods using dir

    print(dir(Section))

    for i in range(101):

        # Initializing the Section class

        init = Section(i)

        # Number of input, object repr, methods
        print(i, init, init.index(None), init.show(0)) # The other methods are handled for the tuple type

        # Errors

        # The length must not be less than 0
        # Output: raise ValueError('Sample larger than population or is negative')

        # If you call the method show and pass as parameter a type other than integer, you'll get a error
        # Examples: object.show(None), object.show(5.2)
        # Output: TypeError: '<' not supported between instances of 'NoneType' and 'int'
        # Output: TypeError: tuple indices must be integers or slices, not float
