class UserShotInput:

    @staticmethod
    def ask_for_position(player, ocean):
        '''
        Ask user for position to shot the ship
        
        Args:
        player():
        ocean(list):
        '''
        columns = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
        rows = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10')
        column_input = ""
        while column_input not in columns:
            column_input = input("\nEnter column (a-j): ")
        row_input = ""
        while row_input not in rows:
            row_input = input("Enter row (1-10): ")
        row_input = rows.index(row_input)
        column_input = columns.index(column_input)
        player.shot(row_input, column_input, ocean)
