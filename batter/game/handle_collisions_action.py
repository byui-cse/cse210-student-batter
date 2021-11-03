import random
from game import constants
from game.action import Action

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
        bricks = cast["bricks"]
        marquee.set_text("")
        for brick in bricks:
            if paddle.get_position().equals(bricks.get_position()):
                description = bricks.get_description()
                marquee.set_text(description) 
