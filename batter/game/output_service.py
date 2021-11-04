""" 
"""
import sys
from game import constants
from asciimatics.widgets import Frame

class OutputService:
    """
    
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            screen (Screen): An Asciimatics Screen.
        """
        self._screen = screen
        
    def clear_screen(self):
        """Clears the Asciimatics buffer for the next rendering.""" 
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)
        self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)

    def draw_actor(self, actor):
        """Renders the given actor's text on the screen.

        Args:
            actor (Actor): The actor to render.

        """ 
        color = actor.get_color()
        if color == 'black':
            color_palette = 0 #black
        elif color == 'red':
            color_palette = 1 #red
        elif color == 'green':
            color_palette = 2 #green
        elif color == 'yellow':
            color_palette = 3 #yellow
        elif color == 'blue':
            color_palette = 4 #blue
        elif color == 'magenta':
            color_palette = 5 #magenta
        elif color == 'cyan':
            color_palette = 6 #cyan
        elif color == 'white':
            color_palette = 7 #white
        
        text = actor.get_text()
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        self._screen.print_at(text, x, y, color_palette)


    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    

    def flush_buffer(self):
        """Renders the screen.""" 
        self._screen.refresh()