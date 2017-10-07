from random import randint


class InsertShip:

    @staticmethod
    def choose_ship(ocean):
        '''
        Inserts ship in board after checking space around it

        Args:
            ocean - object of class ocean

        Return:
            None
        '''
        ships = {"carrier": 5, "battleShip": 4, "cruise": 3, "submarine": 3, "destroyer": 2}
        ship_index = 0
        while ships:
            ship = []
            for k, v in ships.items():
                print(k, "[", v, "space ]")
            choose_ship_input = ""
            while choose_ship_input not in list(ships.keys()):
                choose_ship_input = input("\nChoose ship name: ")
            choose_ship = ships[choose_ship_input]
            position = InsertShip.ship_position()
            ship.append(choose_ship)
            ship.append(position)
            while not ocean.check_space_around(ship):
                print("Bad decision")
                for k, v in ships.items():
                    print(k, "[", v, "space ]")
                ship = []
                choose_ship_input = input("\nChoose ship name: ")
                choose_ship = ships[choose_ship_input]
                position = InsertShip.ship_position()
                ship.append(choose_ship)
                ship.append(position)
            ocean.add_ship(ship[0], ship[1][0], ship[1][1], ship[1][2], ship_index)
            ship_index += 1
            del ships[choose_ship_input]

    @staticmethod
    def ship_position():
        '''
        Takes user input about ship to be inserted

        Return:
            position - list of inputs about ship
        '''
        position = []
        columns = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
        rows = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        ship_column = ""
        while ship_column not in columns:
            ship_column = input("Column of ship (a-j): ")

        ship_row = ""
        while ship_row not in rows:
            ship_row = input("Row of ship(1-10): ")

        position.append(rows.index(ship_row))
        position.append(columns.index(ship_column))

        position_input = input("Choose position:\n"
                               "write\n"
                               "v if vertical\n"
                               "or\n"
                               "h if horizontal\n"
                               "Choose: ")
        if position_input == "v":
            position.append(True)
        elif position_input == "h":
            position.append(False)
        else:
            InsertShip.ship_position()

        return position

    @staticmethod
    def randomize_ships(ocean):
        '''
        Inserts randomly placed ships

        Args:
            ocean - object of class Ocean

        Return:
            None
        '''
        ships = [5, 4, 3, 3, 2]
        ships_index = 0
        for s in ships:
            ship_pos = []
            ship_pos.append(s)
            position = InsertShip.random_position()
            ship_pos.append(position)
            while not ocean.check_space_around(ship_pos):
                ship_pos = []
                ship_pos.append(s)
                position = InsertShip.random_position()
                ship_pos.append(position)
            ocean.add_ship(ship_pos[0], ship_pos[1][0], ship_pos[1][1], ship_pos[1][2], ships_index)
            ships_index += 1

    @staticmethod
    def random_position():
        '''
        Create list of random atributes for ship

        Return:
            list - contains atributes of ship
        '''
        x = randint(0, 9)
        y = randint(0, 9)
        positions = [True, False]
        pos = positions[randint(0, 1)]
        return [x, y, pos]
