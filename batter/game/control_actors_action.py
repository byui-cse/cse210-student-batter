from game import constants
from game.action import Action

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
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
            cast (Cast object): The current game actors.
        """
        direction = self._input_service.get_direction()
        paddle_parts = cast.paddle_parts
        paddle_far_left = paddle_parts[0].get_position().get_x() == 1
        paddle_far_right = paddle_parts[-1].get_position().get_x() == constants.MAX_X - 1
        if paddle_far_left and direction.get_x() == -1:
            return
        if paddle_far_right and direction.get_x() == 1:
            return
        for sect in paddle_parts:
            sect.set_velocity(direction)
