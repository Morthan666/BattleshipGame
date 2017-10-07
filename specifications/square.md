### Class Square

__Instance Attributes__

* `row`
  - data: list
  - description: it's contain whitespaces

* `column`
  - data: list
  - description: it's contain whitespaces

* `is_ship`
  - data: bool
  - description: if is_hit and not is_ship: 'O', elif is_hit and is_ship: 'X', else: ' '

__Instance methods__

* ##### ` __init__(self, row, column, is_ship)`
  
  Construct object square. 

* `hit(self)`
  
  Method to hit ship and set the object to True
  

* `__str__(self, is_player=False, position=None)`

  Returns a string
