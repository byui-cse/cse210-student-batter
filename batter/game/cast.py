from game.actor import Actor
from game import constants
from game.point import Point

class Cast:

    def __init__(self):
        self._setup_base_actors()

    def _setup_base_actors(self):
        self.setup_paddle()
        self.setup_bricks()
        self.setup_ball()
        self.setup_top()
        self.setup_sides()
        self.setup_bottom()

    def setup_paddle(self):
        self._paddle_parts = []
        start_x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y - 1)
        for x in range(start_x, start_x + 11):
            position = Point(x, y)
            paddle = Actor()
            if x == start_x:
                paddle.set_text('╾')
            elif x == start_x + 10:
                paddle.set_text('╼')
            else:
                paddle.set_text('─')
            paddle.set_position(position)
            self._paddle_parts.append(paddle)
    
    def setup_bricks(self):
        self._bricks = []
        for x in range(5, 75):
            for y in range(2, 6):
                position = Point(x, y)
                brick = Actor()
                brick.set_text("*")
                brick.set_position(position)
                self._bricks.append(brick)
    
    def setup_ball(self):
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        position = Point(x, y)
        velocity = Point(1, -1)
        ball = Actor()
        ball.set_text("@")
        ball.set_position(position)
        ball.set_velocity(velocity)
        self._ball = ball

    def setup_top(self):
        self._top_parts = []
        y = 0
        for x in range(constants.MAX_X):
            position = Point(x, y)
            top_part = Actor()
            if x == 0:
                top_part.set_text("╔")
            elif x == constants.MAX_X:
                top_part.set_text("╗")
            else:
                top_part.set_text("═")
            top_part.set_position(position)
            self._top_parts.append(top_part)

    def setup_sides(self):
        self._side_parts = []
        for i in range(2):
            if i == 0:
                x = 0
            else:
                x = constants.MAX_X
            for y in range(1, constants.MAX_Y):
                position = Point(x, y)
                side_part = Actor()
                side_part.set_text("║")
                side_part.set_position(position)
                self._side_parts.append(side_part)

    # def setup_left(self):
    #     self._left_parts = []

    def setup_bottom(self):
        self._bottom_parts = []
        y = constants.MAX_Y
        for x in range(constants.MAX_X):
            position = Point(x, y)
            bottom_part = Actor()
            if x == 0:
                bottom_part.set_text("╚")
            elif x == constants.MAX_X:
                bottom_part.set_text("╝")
            else:
                bottom_part.set_text("═")
            bottom_part.set_position(position)
            self._bottom_parts.append(bottom_part)

    @property
    def paddle_parts(self):
        return self._paddle_parts
    
    @property
    def bricks(self):
        return self._bricks
    
    @property
    def ball(self):
        return self._ball
    
    @property
    def top_parts(self):
        return self._top_parts

    @property
    def side_parts(self):
        return self._side_parts

    @property
    def bottom_parts(self):
        return self._bottom_parts

    @property
    def cast_list(self):
        formatted_cast = [self._paddle_parts, [self._ball], self._bricks, self._top_parts, self._side_parts, self.bottom_parts]
        return formatted_cast
    
    @property
    def npc_list(self):
        return [[self._ball], self._bricks]
