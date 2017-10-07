import os
from UI import UI
from insert_ship import InsertShip


class Game:
    def __init__(self, player1, player2):
        '''
        Construct a Game object

        Args:
            player1 and player2 - objects of class Player

        Return:
            object of class Game
        '''
        self.player1 = player1
        self.player2 = player2

    def user_with_computer_game(self):
        '''
        Flow of user vs computer Game

        Return:
            None
        '''
        ui = UI()
        choice = ui.choose_ships()
        if choice == "1":
            InsertShip.choose_ship(self.player1.ocean)
        else:
            InsertShip.randomize_ships(self.player1.ocean)
        InsertShip.randomize_ships(self.player2.ocean)
        while not self.has_Won():
            os.system("clear")
            print("{:^33}\n".format('Your board:'))
            ui.show_board(self.player1.ocean, True)
            print("\n")
            print("{:^33}\n".format('Enemy board:'))
            ui.show_board(self.player2.ocean)
            self.player1.ai.turn(self.player2.ocean, self.player1)
            self.player2.ai.turn(self.player1.ocean, self.player2)
        os.system("clear")
        print("{:^33}".format(self.who_won() + " won!"))

    def user_with_user_game(self):
        '''
        Flow of user vs user game

        Return:
            None
        '''
        ui = UI()
        choice = ui.choose_ships()
        if choice == "1":
            InsertShip.choose_ship(self.player1.ocean)
        else:
            InsertShip.randomize_ships(self.player1.ocean)
        choice = ui.choose_ships()
        if choice == "1":
            InsertShip.choose_ship(self.player2.ocean)
        else:
            InsertShip.randomize_ships(self.player2.ocean)
        while not self.has_Won():
            os.system("clear")
            print("{:^33}\n".format('Your' + " board:"))
            ui.show_board(self.player1.ocean, True)
            print("\n")
            print("{:^33}\n".format(self.player2.name + "'s board:"))
            ui.show_board(self.player2.ocean)
            self.player1.ai.turn(self.player2.ocean, self.player1)
            os.system("clear")
            print("{:^33}\n".format('Your' + " board:"))
            ui.show_board(self.player2.ocean, True)
            print("\n")
            print("{:^33}\n".format(self.player1.name + "'s board:"))
            ui.show_board(self.player1.ocean)
            self.player2.ai.turn(self.player1.ocean, self.player2)
        os.system("clear")
        print("{:^33}".format(self.who_won() + " won!"))

    def computer_with_computer_game(self):
        '''
        Flow of simulation

        Return:
            None
        '''
        InsertShip.randomize_ships(self.player1.ocean)
        InsertShip.randomize_ships(self.player2.ocean)
        while not self.has_Won():
            ui = UI()
            ui.show_board(self.player1.ocean, True)
            print("\n")
            self.player1.ai.turn(self.player2.ocean, self.player1)
            ui.show_board(self.player2.ocean, True)
            print("\n")
            self.player2.ai.turn(self.player1.ocean, self.player2)
        print("{:^33}".format(self.who_won() + " won!"))

    def who_won(self):
        '''
        Method of checking who won

        Return:
            player.name - string
        '''
        if self.player1.ocean.are_sunk():
            return self.player2.name
        else:
            return self.player1.name

    def has_Won(self):
        '''
        Condition to roll the game until one of the player's ships are sunk

        Return:
            bool
        '''
        if self.player1.ocean.are_sunk() or self.player2.ocean.are_sunk():
            return True
        return False
