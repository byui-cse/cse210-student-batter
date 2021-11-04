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
        self.ball_brick_collision(cast)
        # self.ball.paddle_constraints(cast)
        # self.ball__handle_collision(cast)
        # self.ball_ceiling_collision(cast)
        # self.ball_floor_collision(cast)

    def ball_brick_collision(self, cast):
        bricks = cast["brick"] # there's only one
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0]
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                brick.set_text("")
                ball.set_velocity(Point(-1, 1))

    def paddle_constraints(self, paddle):
        pass
    # Needs to get the position of the paddle.
    # Compare paddle to 0.
    # less then zero set paddle start back to zero
    # If the paddle became more then 69 then reset back to 69

    def ball_paddle_collision(self, paddle, ball):
        pass
        # Needs to loop through the length of the paddle and compare its position with the position of the ball.
        # If the ball postition is equal to any portion of the paddle, bounce.
        # need to return 


    def ball_handle_constraints(self, ball):
        pass
        # Needs to find the position of the ball.
        # Then grab the y value of the ball.
        # The check to see if y equals 0 + 1
        # if yes, bounce the ball.
        # Find the x value of ball.
        # if x equal 0 or Max_X bounce.

    
    def ball_floor_collision(self,cast):
        # balPos = cast["ball"].get_position()
        # if balPos.get_x() == constants.MAX_X or balPos.get_x() == 0 or balPos.get_y() == constants.MAX_Y:
        #     pass

        # if balPos.get_y() == 0:
        #     quit()
        # pass
        # Needs to find the position of the ball.
        # Then grab the y value of the ball.
        # The check to see if y equals of MAX_Y
        # Exit the system
        pass
    
    def ball_ceiling_collision(self, ball):
        pass

