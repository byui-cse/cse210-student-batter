#Tyson

import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.
    Stereotype: 
        Service Provider
    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for up, dn, lt, rt, and shift as a modifer for extra speed.
    """

    def __init__(self, screen):
        """The class constructor."""
        self._screen = screen
        self._keys = {}
        self._keys[119] = Point(0, -1) # w
        self._keys[115] = Point(0, 1) # s
        self._keys[97] = Point(-1, 0) # a
        self._keys[100] = Point(1, 0) # d
        self._keys[87] = Point(0, -3) # W
        self._keys[83] = Point(0, 3) # S
        self._keys[65] = Point(-3, 0) # A
        self._keys[68] = Point(3, 0) # D
        
    def get_direction(self):
        """Gets the selected direction for the given player.
        Returns:
            Point: The selected direction.
        """
        direction = Point(0, 0)
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == -1:
                sys.exit()
            direction = self._keys.get(event.key_code, Point(0, 0))
        return direction