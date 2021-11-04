""" 
"""
import random
from game import constants
from game.actor import Actor
from game.point import Point


class Lives(Actor):
    """

    Stereotype:
        Information Holder

    Attributes: 
        
    """

    def __init__(self):
        """
        
        Args:
            self (Lives): an instance of Lives.
        """
        super().__init__()
        self._lives = constants.NUMBER_OF_LIVES
        self._color = 'cyan'
        self.set_text(f"[Lives Remaining: {self._lives + 1}]")

    def get_lives(self):
        """
        """
        return self._lives

    def set_lives(self, lives):
        """
        """
        self._lives = lives

    def subtract_life(self):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Lives): An instance of Lives.
            _lives (integer): The lives remaining.
        """
        if self._lives > 0:
            self._lives -= 1
        if self._lives < 1:
            self._color = 'red'
        self.set_text(f"[Lives Remaining: {self._lives + 1}]")