from square import Square


class Ship:
    def __init__(self, size, start_row, start_column, is_vertical):
        '''
        Constructs a Ship object

        Args:
            size (int): size of ship
            start_row (int): starting index
            start_column (int): starting index
            is_vertical (bool): contains True if is vertical, otherwise False
        '''
        self.size = size
        self.start_row = start_row
        self.start_column = start_column
        self.is_vertical = is_vertical
        self.squares = []
        self.build_ship()

    def is_sunk(self):
        '''
        Method to check if square is hit.

        Returns:
            (bool): Set the object to True if is hit, otherwise False
        '''
        for item in self.squares:
            if not item.is_hit:
                return False
        return True

    def build_ship(self):
        '''
        Method to build ship depends on attribute is_vertical
        '''
        for i in range(self.size):
            if self.is_vertical:
                self.squares.append(Square(self.start_row + i, self.start_column, True))
            else:
                self.squares.append(Square(self.start_row, self.start_column + i, True))
