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
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]
        
        
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                ball.set_velocity(ball._velocity.bounce_Y())
                bricks.remove(brick)
        
        #If ball bounces off paddle:
        if (paddle.get_position().equals(ball.get_position())
            or ball.get_position().equals(paddle.get_position().add(Point(1,0)))
            or ball.get_position().equals(paddle.get_position().add(Point(2,0)))
            or ball.get_position().equals(paddle.get_position().add(Point(3,0)))
            or ball.get_position().equals(paddle.get_position().add(Point(4,0)))
            or ball.get_position().equals(paddle.get_position().add(Point(5,0)))
            or ball.get_position().equals(paddle.get_position().add(Point(6,0)))
            or ball.get_position().equals(paddle.get_position().add(Point(7,0)))
            or ball.get_position().equals(paddle.get_position().add(Point(8,0)))
            or ball.get_position().equals(paddle.get_position().add(Point(9,0)))
            or ball.get_position().equals(paddle.get_position().add(Point(10,0)))
            ):
            
            ball.set_velocity(ball._velocity.bounce_Y())
       
        #If ball bounces off right wall:
        elif ball.get_position().get_x() == (constants.MAX_X - 1):
            ball.set_velocity(ball._velocity.bounce_X())

        #If ball bounces off left wall:
        elif ball.get_position().get_x() == 1:
            ball.set_velocity(ball._velocity.bounce_X())

        #If ball bounces off floor:
        elif ball.get_position().get_y() == constants.MAX_Y - 1:
            sys.exit()

        #If ball bounces off ceiling
        elif ball.get_position().get_y() == 1:
            ball.set_velocity(ball._velocity.bounce_Y())
        
        paddlex = paddle.get_position().get_x()
        if paddlex == (70):
            x = int(paddle.get_position().get_x() - 2)
            y = int(constants.MAX_Y - 1)
            position = Point(x, y)
            paddle.set_position(position)
        elif paddlex == (2):
            x = int(paddle.get_position().get_x() + 2)
            y = int(constants.MAX_Y - 1)
            position = Point(x, y)
            paddle.set_position(position)
