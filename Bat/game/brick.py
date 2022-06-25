import random
from game import constants
from game.actor import Actor
from game.point import Point



class Brick(Actor):
    def __init__(self,x,y):
        self._position = Point(x,y)
        self._velocity = Point(0,0)
        self._text = "*"
    
    def get_points(self):
        return 5
    
    def reset(self):
        self.move_next()



# TODO: Define the Food class here