from ship import Ship
from square import Square


class Ocean:

    def __init__(self):
        '''
        Constructs an Ocean object and fills board with Square objects

        Return:
            object of class Ocean
        '''
        self.board = []
        self.ships = []
        self.BOARD_SIZE = 10
        self.create_board()

    def are_sunk(self):
        '''
        Cheks if all ships in list ships are sunk

        Returns:
            bool
        '''
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True

    def check_space_around(self, ship_info_list):
        '''
        Checks if ship can be inserted in board

        Args:
            ship_info_list - list with ship atributes

        Returns:
            bool
        '''
        size = ship_info_list[0]
        start_row = ship_info_list[1][0]
        start_column = ship_info_list[1][1]
        is_vertical = ship_info_list[1][2]
        if is_vertical:
            if start_row + size - 1 > 9:
                return False
            for i in range(-1, size+1):
                if start_row + i >= 0 and start_column - 1 >= 0:
                    try:
                        if self.board[start_row+i][start_column - 1].is_ship:
                            return False
                    except IndexError:
                        pass
                if start_row + i >= 0:
                    try:
                        if self.board[start_row + i][start_column].is_ship:
                            return False
                    except IndexError:
                        pass
                if start_row + i >= 0:
                    try:
                        if self.board[start_row+i][start_column + 1].is_ship:
                            return False
                    except IndexError:
                        pass
        else:
            if start_column + size - 1 > 9:
                return False
            for i in range(-1, size + 1):
                if start_row - 1 >= 0 and start_column + i >= 0:
                    try:
                        if self.board[start_row - 1][start_column + i].is_ship:
                            return False
                    except IndexError:
                        pass
                if start_column + i >= 0:
                    try:
                        if self.board[start_row][start_column + i].is_ship:
                            return False
                    except IndexError:
                        pass
                if start_column + i >= 0:
                    try:
                        if self.board[start_row + 1][start_column + i].is_ship:
                            return False
                    except IndexError:
                        pass
        return True

    def add_ship(self, size, start_row, start_column, is_vertical, index):
        '''
        Appends ships list with ship object and inserts it in board

        Args:
            size - int
            start_row - int
            start_column - int
            is_vertical - bool
            index - int

        Return:
            None
        '''
        self.ships.append(Ship(size, start_row, start_column, is_vertical))
        self.insert_ships(index)

    def insert_ships(self, index):
        '''
        Inserts ship of given index in ships list in board

        Args:
            index - int

        Return:
            None
        '''
        for square in self.ships[index].squares:
            self.board[square.row][square.column] = square

    def create_board(self):
        '''
        Fills board list with Square objects

        Return:
            None
        '''
        for i in range(self.BOARD_SIZE):
            self.board.append([])
            for j in range(self.BOARD_SIZE):
                self.board[i].append(Square(i, j, False))
