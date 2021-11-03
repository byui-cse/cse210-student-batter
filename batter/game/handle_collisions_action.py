import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility 
    of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        bricks = cast["brick"] # there's only one
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0]
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                brick.set_text("")
                ball.set_velocity(Point(-1, 1))

        balPos = ball.get_position()
        if balPos.get_x() == constants.MAX_X or balPos.get_x() == 0 or balPos.get_y() == constants.MAX_Y:
            pass

        if balPos.get_y() == 0:
            quit()

