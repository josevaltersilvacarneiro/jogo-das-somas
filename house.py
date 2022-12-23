class House:
    """This class represents the section house.
    A value must be passed as argument when
    instantiate it.

    """

    def __init__(self, value : int) -> None:

        self._value  : int  = value;
        self._status : bool = False;

    @property
    def value(self) -> int:
        return self._value;

    @property
    def status(self) -> bool:
        return self._status

    @status.setter
    def status(self, new_status : bool) -> None:
        self._status = new_status;
