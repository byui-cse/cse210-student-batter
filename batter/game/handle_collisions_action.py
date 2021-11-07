"""Module handle_collisions_action containing class HandleCollisionsAction
and its corresponding methods. It handles actor's collisions.
"""
from game import constants
from game.action import Action
from game.point import Point


class HandleCollisionsAction(Action):
    """A code template for checking collisions. The responsibility of 
    this class of objects is to check actor's collisions and set their
    velocity afterwards.
    
    Stereotype:
        Controller
    
    Attributes:
        keep_playing (boolean): Flag that determines whether the game continues or not.
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (HandleCollisionsAction): An instance of HandleCollisionsAction.
        """
        super().__init__()
        self.keep_playing = True
        
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0]      # ball 
        paddle = cast["paddle"][0]  # paddle
        self.bricks = cast["brick"] # bricks
        score = cast["score"][0]    #score
        paddle_range = []           # a list with the position of each paddle's component.
        lives = cast["lives"][0]    # lives

        self.checkPlay()
        
        brick_index = 0
        for brick in self.bricks:
            if ball.get_position().equals(brick.get_position()):
                direction = ball.get_velocity().reverse_y()
                direction = direction.random_velocity_generator() 
                ball.set_velocity(direction)
                del self.bricks[brick_index]
                score.add_points(1)
            brick_index += 1

        # checking boundaries
        check_x_limits = ball.get_position().get_x()
        check_y_limits = ball.get_position().get_y()

        if check_x_limits >= constants.MAX_X -1 or check_x_limits <= 1:
            direction = ball.get_velocity().reverse_x()
            ball.set_velocity(direction)

        if check_y_limits <= 1:
            direction = ball.get_velocity().reverse_y()
            direction = direction.random_velocity_generator()
            ball.set_velocity(direction)

        #if check_y_limits == constants.MAX_Y -1:
        if check_y_limits == paddle.get_position().get_y():
            x = paddle.get_position().get_x()
            for value in range(constants.PADDLE_LENGTH): 
                paddle_range.append(x + value)
            ball_x = ball.get_position().get_x()
           
            if ball_x in paddle_range:   #if paddle hits the ball
                new_y = ball.get_velocity().reverse_y()
                ball.set_velocity(new_y)

            elif lives.get_lives():  #if paddle misses the ball
                lives.subtract_life()

                x_ball = int(constants.MAX_X / 2)
                y_ball = int(constants.MAX_Y - 2)

                x_paddle = x_ball - len(paddle_range) // 2
                y_paddle = int(constants.MAX_Y - 1)
                paddle_pos = Point(x_paddle, y_paddle)
                paddle.set_position(paddle_pos)

                ball_pos = Point(x_ball, y_ball)
                ball.set_position(ball_pos)
                           
            else:
                self.keep_playing = False

    def checkPlay(self):
        """Checks the condition of the game.

        Args:
            self (Actor): An instance of Actor.

        Returns:
            keep_playing (boolean): The flag determining whether the game continues or not.
        """
        if not self.bricks:
            self.keep_playing = False
        return self.keep_playing