### Class Game

__Instance Attributes__

* `player1`
  - data: obj
  - description: objects of class Player

* `player2`
  - data: obj
  - description: objects of class Player


__Instance methods__

* ##### ` __init__(self, player1, player2)`

  Construct a Game object
  Return object of class Game

* `user_with_computer_game(self)`

  Flow of user vs computer Game
  Return None

* `user_with_user_game(self)`

  Flow of user vs user game
  Return None

* `computer_with_computer_game(self)`

  Flow of simulation
  Return None

* `who_won(self)`

  Method of checking who won
  player.name - string

* `has_Won(self)`

  Condition to roll the game until one of the player's ships are sunk
  Return bool


* `__str__(self)`

  Updated board after each move
