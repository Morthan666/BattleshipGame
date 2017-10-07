### Class Ocean

__Instance Attributes__

* `board`
  - data: list
  - description: list of object Square Class

* `ships`
  - data: list
  - description: list of object Ship Class

 * `ships_are_sunk`
 - data: bool
 - description: True if every ship is_sunk, else False


__Instance methods__

* ##### ` __init__(self)`

  Create two empty lists (board, ships).
  Start method create_board.


* `are_sunk(self)`

  Sets the object's * are_sunk * attribute to True

* `check_space_around(self, ship_info_list)`

  Sets the object's * are_sunk * attribute to True

* `add_ships(self, size, start_row, start_column, is_vertical, index)`

  Sets the object's * are_sunk * attribute to True


* `create_board(self)`

  Append board objects from Square Class

* `insert_ship(self, index)`

  Insert ship in board


* `__str__(self)`

  Updated board after each move
