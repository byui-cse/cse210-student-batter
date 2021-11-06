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

        #self.ball_paddle_collision(cast)
        self.ball_ceiling_collision(cast)
        self.ball_floor_collision(cast)
        self.ball_wall_collision(cast)
        # self.paddle_boundaries (cast)
        # self.ball_paddle_boundaries(cast)


    def ball_brick_collision(self, cast):
        bricks = cast["brick"]

        ball = cast["ball"][0]# bball brick collision get ball position equal brick get position
        for brick in bricks:
            if ball.get_position().equals(brick.get_position()):
                cast["brick"].remove(brick)
                velocity = ball.get_velocity()
                ball.set_velocity(velocity.reverse_y())
         
        
                #ball.reverse() #ball.set_velocity(ball.get_veloctiy.reveser())  
    # def paddle_boundaries (self, cast):
    #     paddle = cast["paddle"]
    #     pass
    # Needs to get the position of the paddle.
    # Compare paddle to 0.
    # less then zero set paddle start back to zero
    # If the paddle became more than max set back to max

    def ball_paddle_collision(self,cast):

        paddle = cast["paddle"][0]
        ball = cast["ball"][0]# bball brick collision get ball position equal brick get position

        paddle_x_position = paddle.get_position().get_x()
        paddle_y_position = paddle.get_position().get_y()
        ball_x_position = ball.get_position().get_x()
        ball_y_position = ball.get_position().get_y()
        
        if (ball_y_position == paddle_y_position and ball_x_position >= paddle_x_position and ball_x_position <= paddle_x_position + len(paddle.get_text())):
            velocity = ball.get_velocity()
            ball.set_velocity(velocity.reverse_y())
        
 
        pass
        # Needs to loop through the length of the paddle and compare its position with the position of the ball.
        # If the ball postition is equal to any portion of the paddle, bounce.
        # need to return 


    def ball_wall_collision(self, cast):
        ball = cast["ball"][0]
        position = ball.get_position()
        ball_x = position.get_x()
        if ball_x >= constants.MAX_X or ball_x <= 0:
            velocity = ball.get_velocity()
            ball.set_velocity(velocity.reverse_x())


        
        # Needs to find the position of the ball.
        # Then grab the y value of the ball.
        # The check to see if y equals 0 + 1
        # if yes, bounce the ball.
        # Find the x value of ball.
        # if x equal 0 or Max_X bounce.

    
    def ball_floor_collision(self,cast):
        ball = cast["ball"][0]
        position = ball.get_position()
        ball_y = position.get_y()
        if ball_y >= constants.MAX_Y +2:
            sys.exit()
            # velocity = ball.get_velocity()
            # ball.set_velocity(velocity.reverse_y())
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
    
    def ball_ceiling_collision(self, cast):

        ball = cast["ball"][0]
        position = ball.get_position()
        ball_y = position.get_y()
        if ball_y == 0:
            velocity = ball.get_velocity()
            ball.set_velocity(velocity.reverse_y())


