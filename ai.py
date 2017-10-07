from random import randint
from user_shot_input import UserShotInput


class Ai:
    def __init__(self, level):
        '''
        Construct AI object

        Args:
            level - str

        Return:
            Ai instance
        '''
        self.level = level
        self.coordinates_memory = (0, 0)

    def turn(self, ocean, player):
        '''
        Assigns Ai move based on level given

        Args:
            ocean - object class Ocean
            player - object class Player

        Return:
            None
        '''
        if self.level == "Easy":
            self.easy(ocean.board)
        elif self.level == "Medium":
            self.medium(ocean.board)
        elif self.level == "Hard":
            self.hard(ocean)
        else:
            UserShotInput.ask_for_position(player, ocean)

    def easy(self, board):
        '''
        Computer tactics on level easy

        Args:
            board - matrix of squares

        Return:
            None
        '''
        x = randint(0, 9)
        y = randint(0, 9)
        while board[x][y].is_hit:
            x = randint(0, 9)
            y = randint(0, 9)
        board[x][y].hit()

    def medium(self, board):
        '''
        Computer tactics on level medium

        Args:
            board - matrix of squares

        Return:
            None
        '''
        for i in board:
            for j in i:
                if not j.is_hit:
                    j.hit()
                    return

    def hard(self, ocean):
        '''
        Computer tactics on level hard

        Args:
            ocean - object class Ocean

        Return:
            None
        '''
        for row in ocean.board:
            for cell in row:
                if cell.is_hit and cell.is_ship and not self.is_part_of_sunken_ship(ocean, cell):
                    next_target = self.check_neighbours(ocean, cell)
                    if next_target:
                        next_target.hit()
                        return
        self.skip_squares(ocean.board)

    def is_part_of_sunken_ship(self, ocean, cell):
        '''
        Checks if square is part of sunk ship

        Args:
            ocean - object class ocean
            cell - object of class Square

        Return:
            bool
        '''
        for ship in ocean.ships:
            if cell in ship.squares:
                if ship.is_sunk():
                    return True
        return False

    def check_neighbours(self, ocean, cell):
        '''
        Finds unhit neighbour of given cell

        Args:
            ocean - object class ocean
            cell - object of class Square

        Return:
            neighbour - object of class Square
        '''
        for i in (-1, 1):
            try:
                neighbour = ocean.board[cell.row - i][cell.column]
                if not neighbour.is_hit:
                    return neighbour
            except IndexError:
                pass
            try:
                neighbour = ocean.board[cell.row][cell.column - i]
                if not neighbour.is_hit:
                    return neighbour
            except IndexError:
                continue

    def skip_squares(self, board):
        '''
        Iterates over every second square in board

        Args:
            board - matrix of squares

        Return:
            None
        '''
        for row in board:
            for cell in row:
                if cell.row % 2 == 0:
                    if cell.column % 2 == 0:
                        if not cell.is_hit:
                            cell.hit()
                            return
                    else:
                        continue
                else:
                    if cell.column % 2 == 0:
                        continue
                    else:
                        if not cell.is_hit:
                            cell.hit()
                            return
