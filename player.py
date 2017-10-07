from ai import Ai
from ocean import Ocean


class Player:

    def __init__(self, name, level):
        '''
        Create Player class object

        Arg:
            name - string
            level - string

        Return:
            object of class Player
        '''
        self.ocean = Ocean()
        self.ai = Ai(level)
        self.name = name

    def shot(self, row, column, ocean):
        '''
        Hits square of given indexes in board matrix

        Args:
            row - int
            column - int
            ocean - object of class Ocean

        Return:
            None
        '''
        ocean.board[row][column].hit()
