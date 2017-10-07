### Class Ship

__Instance Attributes__

* `size`
  - data: int
  - description: size of ship

* `is_vertical`
  - data: bool
  - description: contains True if player decide, otherwise contains False.

* `start_row`
  - data: int
  - description: starting index 

* `start_column`
  - data: int
  - description: starting index


__Instance methods__

* ##### ` __init__(self, size, start_row, start_column, is_vertical)`
  
  Create ship, it's a list. 

* `is_sunk(self)`
  
  Method to check if square is hit, then set the object to True, otherwise False

* `build_ship(self)`
  
  String

* `__str__(self)`

  Join
