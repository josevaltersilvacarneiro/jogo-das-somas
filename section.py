from random import sample

class Section(tuple):

    """
        This class creates a new type of data. The type
        Section is a tuple of unrepeated random elements.
    """
   
    def __new__(self, length : int):

        return super().__new__(
                    Section,
                    sample(range(1, length + 1), length)
                )

    # private

    def _not_contain(self, number : int) -> bool:

        return number not in self.__iter__()

    # public

    def show(self, index : int) -> int:

        if index < self.__len__():
            return self.__getitem__(index)
        
        return None

    def index(self, number : int, return_value = None) -> int:

        if self._not_contain(number):
            return return_value
        
        return super().index(number)
