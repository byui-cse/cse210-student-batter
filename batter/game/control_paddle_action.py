"""Module control_paddle_action containing class ControlPaddleAction
and its corresponding methods. It translates user input into paddle's
movement.
"""
from game import constants
from game.action import Action
from game.point import Point

class ControlPaddleAction(Action):
    """A code template for controlling the paddle. The responsibility of this
    class of objects is translate user input into paddle's movement.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        x = direction.get_x() * constants.PADDLE_SPEED_FACTOR
        y = direction.get_y()
                           
        direction = Point(x, y)
        paddle = cast["paddle"][0]
        paddle.set_velocity(direction)