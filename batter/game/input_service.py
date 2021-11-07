
"""Module input_service containing class InputService
and its corresponding methods. It detects user's input.
"""
import sys
import msvcrt
from game.point import Point
from asciimatics.event import KeyboardEvent


class InputService:
    """Detects player input. The responsibility of the class 
    of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for lt, rt.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
            screen (Screen): An instance of Screen.
        """
        self._screen = screen
        self._keys = {}

        self._keys[97] = Point(-1, 0)  # a
        self._keys[100] = Point(1, 0) # d
        
    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.
        
        Args:
            self (InputService): An instance of InputService.
        
        Returns:
            Point: The selected direction.
        """
        direction = Point(0, 0)
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27:
                 sys.exit()
                                      
            direction = self._keys.get(event.key_code, Point(0, 0))
            while msvcrt.kbhit(): # to flush keyboard buffer. It solves batter's inertia.
                msvcrt.getch()
        return direction
