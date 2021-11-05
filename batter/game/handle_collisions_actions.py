from batter.game.constants import MAX_X, MAX_Y
from game.actions.action import Action

class Handle_collisions_actions(Action):
    "This class go into affect when the ball touches an object in the game"

    def execute(self,cast):
        "This detects weather the ball hits a wall/ paddle, or a brick"
        ball = cast["ball"][0]
        brick = cast["brick"]
        paddle = cast["paddle"]
        if ball.get_position().get_y() >= MAX_Y:
            return False
        elif ball.get_position().get_x() <= 0 or ball.get_position().get_x() >= MAX_X or ball.get_position().get_y() <= 0:
            self.change_direciton(ball)
        for single_paddle in paddle:    
            if ball.get_position().equals(single_paddle.get_position):
                self.change_direciton(ball)
        for single_brick in brick:
            if ball.get_poition().equals(single_brick.get_position()):
                self.hit_brick(brick, single_brick)
                self.change_direciton(ball)

    def hit_brick(self,brick,single_brick):
        "This will delete the brick and add points then call the change direction function"
        index = brick.index(single_brick)
        brick.pop(index)
        self.points(self)

    def change_direciton(self,ball):
        "Changes the direction of the ball"
        V = ball.get_velocity()
        ball.set_velocity(V.reverse())