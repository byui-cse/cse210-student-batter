from game import constants
from game.actor import Actor
from game.point import Point

class Bat(Actor):
    """A limbless reptile. The responsibility of Snake is keep track of its segments. It contains methods for moving and growing among others.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The snake's body (a list of Actor instances)
    """
    def __init__(self):
        self._position = Point(-constants.MAX_X + 8 , constants.MAX_Y - 2 )
        self._velocity = Point(4,0)
        self._text = "=========="
    
    def right_or_left(self,point):
        self._velocity = point

    def bat_collision(self,point):
        for i in range(10):
            if point.get_position().get_x() == self.get_position().get_x() + i and point.get_position().get_y() == constants.MAX_Y - 2: 
                return True
