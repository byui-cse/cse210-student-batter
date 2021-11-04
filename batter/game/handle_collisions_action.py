import random
from game.constants import MAX_X, MAX_Y
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        '''
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                ball.set_velocity(Point.reverse(self))

        #If ball bounces off paddle:
        if paddle.get_position().equals(ball.get_position()):
            ball.set_velocity(Point.bounce_X)
        
        #If ball bounces off right wall:
        if ball.get_position() == (MAX_X):
            ball.set_velocity(Point.bounce_Y)

        #If ball bounces off left wall:
        if ball.get_position() == (Point.get_x, 4):
            ball.set_velocity(Point.bounce_Y)

        #If ball bounces off ceiling:
        if ball.get_position().equals(Point(1, Point.bounce_Y)):
            ball.set_velocity(Point.bounce_X)'''