class Square:

    def __init__(self, row, column, is_ship):
        '''
        Constructs a Square object

        Args:
            row (list): list of row
            column (list): list of column
            is_ship (bool): 
            is_hit (bool):
        '''
        self.row = row
        self.column = column
        self.is_ship = is_ship
        self.is_hit = False

    def hit(self):
        '''
        Method to hit a ship

        Returns:
            (bool): True when is hit
        '''
        self.is_hit = True

    def __str__(self, is_player=False, position=None):
        '''
        

        Args:
            is_player (bool): 
            position (bool):

        Returns:
            (str): 
        '''
        if self.is_hit and self.is_ship:
            return "X"
        elif self.is_hit and not self.is_ship:
            return "O"
        elif is_player and self.is_ship:
            return "⌧"
        else:
            return "~"
