### Class Ai

__Instance Attributes__

* `level`
  - data: string
  - description: level of the game: easy, medium, hard



__Instance methods__

* ##### ` __init__(self, level)`
  
  Construct AI object



* `turn(self, ocean, player)`

  Assigns Ai move based on level given
  Return: None
          
* `easy(self, board)`
   Computer tactics on level easy
   Return None

* `medium(self, board)`
   Computer tactics on level medium
   Return None

* `hard(self, ocean)`
   Computer tactics on level hard
   Return None

* `is_part_of_sunken_ship(self, ocean, cell)`
   Checks if square is part of sunk ship
   Return bool

* `check_neighbours(self, ocean, cell)`
   Finds unhit neighbour of given cell
   Return neighbour - object of class Square

* `skip_squares(self, board)`
   Iterates over every second square in board
   Return None

