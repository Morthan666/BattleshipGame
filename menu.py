from UI import UI
from game import Game
from player import Player


class Menu:

    def menu(self):
        '''
        Choose mode of the game

        Return:
            None
        '''
        ui = UI()
        ui.welcom()
        name = ui.ask_name()
        ui.game_type()
        menu_option = input("Choose option: ")
        if menu_option == '1':
            self.difficulty_choose_with_computer(name)
        elif menu_option == '2':
            self.difficulty_choose_multiplayer(name)
        elif menu_option == '3':
            self.difficulty_computer_with_computer()
        else:
            SystemExit()

    def difficulty_choose_multiplayer(self, first_player):
        '''
        Create players and game object for user vs user game

        Args:
            first_player - string

        Return:
            None
        '''
        ui = UI()
        sec_player = ui.ask_for_sec_player_name()
        player1 = Player(first_player, " ")
        player2 = Player(sec_player, " ")
        game = Game(player1, player2)
        game.user_with_user_game()

    def difficulty_choose_with_computer(self, name):
        '''
        Create players and game object for user vs computer game

        Args:
            name - string

        Return:
            None
        '''
        ui = UI()
        ui.difficulty_type()
        difficulty = ""
        while difficulty not in ('1', '2', '3'):
            difficulty = input("Choose difficulty: ")
        if difficulty == '1':
            player1 = Player(name, " ")
            player2 = Player("computer", "Easy")
        elif difficulty == '2':
            player1 = Player(name, " ")
            player2 = Player("computer", "Medium")
        elif difficulty == '3':
            player1 = Player(name, " ")
            player2 = Player("computer", "Hard")
        game = Game(player1, player2)
        game.user_with_computer_game()

    def difficulty_computer_with_computer(self):
        '''
        Create players and game object for computer vs computer game

        Return:
            None
        '''
        ui = UI()
        game_levels = ['Easy', 'Medium', 'Hard']
        difficulty1 = ''
        while difficulty1 not in game_levels:
            difficulty1 = input("Choose difficulty for first computer (Easy, Medium, Hard): ")
        difficulty2 = ''
        while difficulty2 not in game_levels:
            difficulty2 = input("Choose difficulty for second computer (Easy, Medium, Hard): ")
        player1 = Player(difficulty1 + " AI", difficulty1)
        player2 = Player(difficulty2 + " AI", difficulty2)
        game = Game(player1, player2)
        game.computer_with_computer_game()
