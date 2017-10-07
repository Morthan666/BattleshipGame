class UI:

    def choose_ships(self):
        '''Ask user how to set the ships'''
        choice = "a"
        while choice != "1" and choice != "2":
            choice = input("\nWould you like to:\n"
                           "1.Set your ship positions\n"
                           "2.Randomize your ship positions\n"
                           )
        return choice

    def show_board(self, ocean, is_players=False):
        '''
        Show board with frame

        Args:
            ocean(list)
            is_players(bool):
        '''
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        print('{:^3}'.format(''), end='')
        for letter in letters:
            print('{:^3}'.format(letter), end='')
        print()
        for i in range(10):
            print('{:^3}'.format(i+1), end='')
            for j in range(len(ocean.board)):
                if is_players:
                    print('{:^3}'.format(str(ocean.board[i][j].__str__(is_players))), end='')
                else:
                    print('{:^3}'.format(str(ocean.board[i][j])), end='')
            print()

    def ask_name(self):
        '''Ask user for a name'''
        name = input("\nWhat's your name? ")
        return name

    def welcom(self):
        '''Welcome text'''
        print("WELCOME IN BATTLESHIP!")

    def game_type(self):
        '''Show menu to choose game option'''
        print('\nChoose game type:\n'
              '1.Play with computer\n'
              '2.Play with other player\n'
              '3.Computer-Computer game\n'
              '4.Exit\n')

    def difficulty_type(self):
        '''Show difficulty level'''
        print('\nChoose difficulty level:\n'
              '1.Easy\n'
              '2.Medium\n'
              '3.Hard\n')

    def ask_for_sec_player_name(self):
        '''Ask for secon player name'''
        name = input("What's your name? ")
        return name
