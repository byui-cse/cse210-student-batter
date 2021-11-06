import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 2)
    position = Point(x, y)
    paddle = Actor()
    paddle.set_text("═══════════")
    paddle.set_position(position)
    cast["paddle"] = [paddle]

    cast["brick"] = []
    for x in range(5, 75):
        for y in range(2, 6):
            position = Point(x, y)
            brick = Actor()
            brick.set_text("■ ")
            brick.set_position(position)
            cast["brick"].append(brick)

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    position = Point(x, y) #Start at the half part of the ball
    velocity = Point(1, -1) 
    ball = Actor()
    ball.set_text("@")
    ball.set_position(position)
    ball.set_velocity(velocity)
    cast["ball"] = [ball]

    cast["bottom_barrier"] = []
    x = int(0)
    y = int(constants.MAX_Y - 1)
    for x in range(0, constants.MAX_X):
        position = Point(x, y)
        barrier = Actor()
        barrier.set_text("")
        barrier.set_position(position)
        cast["bottom_barrier"].append(barrier)

    cast["top_barrier"] = []
    x = int(0)
    y = int(1)
    for x in range(0, constants.MAX_X):
        position = Point(x, y)
        barrier = Actor()
        barrier.set_text("")
        barrier.set_position(position)
        cast["top_barrier"].append(barrier)

    cast["side_barrier"] = []
    for y in range(0, constants.MAX_Y):
        position = Point(1, y)
        barrier = Actor()
        barrier.set_text("")
        barrier.set_position(position)
        cast["side_barrier"].append(barrier)
    for y in range(0, constants.MAX_Y):
        position = Point(constants.MAX_X -1, y)
        barrier = Actor()
        barrier.set_text("")
        barrier.set_position(position)
        cast["side_barrier"].append(barrier)
    
    
    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_acition = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_acition]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)