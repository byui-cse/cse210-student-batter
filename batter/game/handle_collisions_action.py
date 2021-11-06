import sys
import random
import sys
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
        self.ball_brick_collision(cast)
        self.ball_paddle_collision(cast)
        self.ball_ceiling_collision(cast)
        self.ball_floor_collision(cast)
        self.ball_wall_collision(cast)
        self.paddle_boundaries(cast)


    def ball_brick_collision(self, cast):
        """The responsibility of this class of objects is to update 
        the game state when actors collide specifically ball to brick collision
        Arg: 
            bricks cast[bricks]
            ball cast[ball]
    """
        bricks = cast["brick"]
        ball = cast["ball"][0]# bball brick collision get ball position equal brick get position
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                cast["brick"].remove(brick)
                velocity = ball.get_velocity()
                ball.set_velocity(velocity.reverse_y())

    def ball_paddle_collision(self,cast):
        """The responsibility of this class of objects is to update 
        the game state when actors collide specifically ball to paddle collision 
    """

        paddle = cast["paddle"][0]
        ball = cast["ball"][0]# bball brick collision get ball position equal brick get position

        paddle_x_position = paddle.get_position().get_x()
        paddle_y_position = paddle.get_position().get_y()
        ball_x_position = ball.get_position().get_x()
        ball_y_position = ball.get_position().get_y()
        
        if (ball_y_position == paddle_y_position +2 
            and ball_x_position >= paddle_x_position 
            and ball_x_position <= paddle_x_position + len(paddle.get_text())):
            velocity = ball.get_velocity()
            ball.set_velocity(velocity.reverse_y())
        pass
    def ball_wall_collision(self, cast):
        """The responsibility of this class of objects is to update 
        the game state when actors collide specifically ball to wall collision 
    """
        ball = cast["ball"][0]
        position = ball.get_position()
        ball_x = position.get_x()
        if ball_x >= constants.MAX_X or ball_x <= 0:
            velocity = ball.get_velocity()
            ball.set_velocity(velocity.reverse_x())

    def ball_floor_collision(self,cast):
        """The responsibility of this class of objects is to update 
        the game state when actors collide specifically ball to floor collision 
    """
        ball = cast["ball"][0]
        position = ball.get_position()
        ball_y = position.get_y()
        if ball_y >= constants.MAX_Y +2: # - 1 to test but +2 to run game
            sys.exit()
    
    def ball_ceiling_collision(self, cast):
        """The responsibility of this class of objects is to update 
        the game state when actors collide specifically ball to ceiling collision 
    """

        ball = cast["ball"][0]
        position = ball.get_position()
        ball_y = position.get_y()
        if ball_y == 0:
            velocity = ball.get_velocity()
            ball.set_velocity(velocity.reverse_y())

    def paddle_boundaries(self,cast):
        """The responsibility of this class of objects is to update 
        the game state when actors collide specifically paddle to wall
    """
        paddle = cast["paddle"][0]
        position = paddle.get_position()
        paddle_x = position.get_x()
        paddle_y = position.get_y()
        if paddle_x + len(paddle.get_text()) >= constants.MAX_X:
            velocity = paddle.get_velocity()
            paddle.set_velocity(Point(0,0))
            paddle.set_position(Point(paddle_x-3,paddle_y))
        elif paddle_x <= 0:
            paddle.set_velocity(Point(0,0))
            paddle.set_position(Point(paddle_x+3,paddle_y))


