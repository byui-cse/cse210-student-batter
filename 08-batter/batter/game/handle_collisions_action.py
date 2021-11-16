from operator import pos
import sys
import random
from game import constants
from game.action import Action
from .point import Point
class HandleCollisionsAction(Action):
    """
        handles the collision between the ball and the bricks
        also handles the collision between the ball and the bat

        This is a controller class
    """
    def execute(self, cast):
        paddle = cast['paddle'][0]
        brick = cast['brick'][0]
        ball = cast['ball'][0]
        paddle_position = paddle.get_position()
        position = ball.get_position()
        velocity = ball.get_velocity()
        
        if paddle_position.get_y() - 1 == position.get_y():
            min_x = paddle_position.get_x()
            max_x = min_x + len(paddle.get_text())
            if position.get_x() >= min_x and position.get_x() <= max_x:
                velocity.set_y(velocity.get_y() * -1)
                ball.set_velocity(velocity)
        # This checks if the ball was missed by the paddle. Then it will end the game
            else:
                sys.exit()
        if position.get_x() >= constants.MAX_X - 2:
            velocity.set_x(velocity.get_x() * -1)
            ball.set_velocity(velocity)
        if position.get_x() <= constants.MIN_X + 2:
            velocity.set_x(velocity.get_x() * -1)
            ball.set_velocity(velocity)    
        for n in cast['brick']:
            if n.get_position().equals(position): 
                new_y = velocity.get_y() * -1
                new_x = random.randint(-2,2)
                new_velocity = Point(new_x, new_y)
                cast['brick'].remove(n)
                ball.set_velocity(new_velocity)
            
