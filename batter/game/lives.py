"""Module lives containing class Lives and its corresponding
methods. It keeps track of player's lives.
"""
from game import constants
from game.actor import Actor


class Lives(Actor):
    """Tracks lives. The responsibility of Lives is 
    to keep track of the actor's remaining lives,
    and its appearance.

    Stereotype:
        Information Holder

    Attributes: 
        _color (string): The actor's color.
        _lives (integer): The given lives.        
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Lives): An instance of Lives.
        """
        super().__init__()
        self._lives = constants.NUMBER_OF_LIVES
        self._color = 'cyan'
        self.set_text(f"[Lives Remaining: {self._lives + 1}]")

    def get_lives(self):
        """Returns the remaining lives.

        Args:
            self(Lives): An instance of Lives.
        """
        return self._lives

    def set_lives(self, lives):
        """Set lives to the given value.
        
        Args:
            self (Lives): An instance of Lives.
            _lives (int): the lives remaining.
        """
        self._lives = lives

    def subtract_life(self):
        """Subtracts one live from the total and updates the text.
        
        Args:
            self (Lives): An instance of Lives.
            _lives (integer): The lives remaining.
        """
        if self._lives > 0:
            self._lives -= 1
        if self._lives < 1:
            self._color = 'red'
        self.set_text(f"[Lives Remaining: {self._lives + 1}]")