"""Module main containing method main that handles all
the datatype objects for the game."""
import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_paddle_action import ControlPaddleAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen
from game.score import Score
from game.lives import Lives


def main(screen):
    """Code for the entry point of the program.

    Stereotype:
        Structurer
    Args:
        screen (Screen): An instance of Screen.
    """
    # create the cast {key: tag, value: list}
    cast = {}

    # paddle actor
    paddle = Actor()
    x = int(constants.MAX_X / 2) - constants.PADDLE_LENGTH // 2
    y = int(constants.MAX_Y - 1)
    position = Point(x, y)
    paddle.set_text("▄" * constants.PADDLE_LENGTH) #Alt+220
    paddle.set_position(position)
    paddle.set_color('magenta')
    cast["paddle"] = [paddle]

    # brick actors
    cast["brick"] = []
    for column in range(constants.BRICKS_LEFT_MARGIN, constants.MAX_X - constants.BRICKS_LEFT_MARGIN):
        for row in range(2, 6):
            brick = Actor()
            position = Point(column, row)
            brick.set_text("▓") #Alt+178
            brick.set_position(position)
            brick.set_color('blue')
            cast["brick"].append(brick)

    # ball actor
    ball = Actor()
    x = int(random.randint(1, constants.MAX_X))
    y = int(random.randint(constants.MAX_Y // 2, constants.MAX_Y - 1))
    position = Point(x, y)
    velocity = Point(1, -1)
    ball.set_text("▄")  #Alt+220
    ball.set_position(position)
    ball.set_velocity(velocity)
    ball.set_color('magenta')
    cast["ball"] = [ball]
    
    # score actor
    score = Score()
    x = 1
    y = constants.MAX_Y
    position = Point(x, y)
    score.set_position(position)
    cast["score"] = [score]

    # lives actor
    lives = Lives()
    x = constants.MAX_X - len(lives.get_text()) - 1
    y = constants.MAX_Y
    position = Point(x, y)
    lives.set_position(position)
    cast["lives"] = [lives]

    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_paddle_action = ControlPaddleAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_paddle_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)