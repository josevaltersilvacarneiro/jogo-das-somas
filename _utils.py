"""This file stores useful functions.

"""

def convert(section_row : int, house_column : int, dimension : int) -> tuple:
    """This function calculates the inverse of
    its parameters. For example, If it's called
    receiving a section and the index house, it
    will return the row and column. The contrary
    is also true; that is, if it's called recei-
    ving a row and column, it will return the
    section and index house. For both cases, you
    must inform the dimension.

    """

    if dimension < 2:
        raise ValueError('The minimum dimension is 2');
    elif not 0 <= section_row < pow(dimension, 2) or not 0 <= house_column < pow(dimension, 2):
        raise ValueError('The value of the other parameters doens\'t match the dimension');

    inv_rs = (section_row // dimension) * dimension + house_column // dimension;
    inv_ci = (section_row  % dimension) * dimension + house_column  % dimension;

    return inv_rs, inv_ci;
