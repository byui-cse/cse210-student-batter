import random
import sys
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
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)
        velocity = Point(1, -1)

        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        bottom_barrier = cast["bottom_barrier"]
        top_barrier = cast["top_barrier"]
        side_barrier = cast["side_barrier"]

        # TypeError: 'method' object is not subscriptable
        # ball_name = random.choice["@", "&", "§", "#", "%"]

        ball.set_text("@")

        # Makes the brick disappear when hit
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                brick.set_text("")
                ball.set_velocity(ball.get_velocity().mirror())

        # Game ends if falls outside the paddle. It touches an invisible barrier
        for bar in bottom_barrier:
            if ball.get_position().equals(bar.get_position()):
                sys.exit()

        # Ball bounces back if it touches an invisible top barrier
        for bar in top_barrier:
            if ball.get_position().equals(bar.get_position()):
                ball.set_velocity(ball.get_velocity().mirror())

        # Ball bounces back if it touches an invisible side barrier
        for bar in side_barrier:
            if ball.get_position().equals(bar.get_position()):
                ball.set_velocity(ball.get_velocity().v_mirror())

        # Makes the ball bounce on the paddle
        for i in range(0, 11):
            if ball.get_position().equals(paddle.get_position().add(Point(i, 0))):
                ball.set_text("&")
                ball.set_velocity(ball.get_velocity().mirror())
   