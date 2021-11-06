from game import constants
from game.actor import Actor
from game.point import Point

class Ball(Actor):

    def __init__(self):
        self._position = Point(30, 10)
        self._velocity = Point(-1,1)
        self.set_text("o")

    def ball_collision(self, list):
        x = self.get_velocity().get_x()
        y = self.get_velocity().get_y()
        for i in list:
            if self.get_position().get_y() == i.get_position().get_y():
                x = self.get_velocity().get_x()
                y = -self.get_velocity().get_y()
                self.set_velocity(Point(x,y))
                return i
        
        
    
    def wall_bounce(self):
        x = self.get_velocity().get_x()
        y = self.get_velocity().get_y()

        if self.get_position().get_y() == -constants.MAX_Y - 1:
            x = self.get_velocity().get_x()
            y = -self.get_velocity().get_y()
        
        if self.get_position().get_x() == constants.MAX_X - 1:
            x = -self.get_velocity().get_x()
            y = self.get_velocity().get_y()
        
        self.set_velocity(Point(x,y))
    
    def missed(self):
        if self.get_position().get_y() == constants.MAX_Y - 1:
            return True
        else:
             return False    
        
    
    def bounce(self):
        x = self.get_velocity().get_x()
        y = self.get_velocity().get_y()
        self.set_velocity(Point(x,-y))