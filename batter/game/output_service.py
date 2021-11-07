""" imports constants from game. Imports frame from asciimatics.widgets.
A class of OutputService.
Module output_service containing class OutputService and its corresponding methods. 
It draws the actors on the terminal.

"""
from game import constants


class OutputService:
    """Outputs the game state. The responsibility of the class of objects 
    is to draw the game state on the terminal.
    
    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (OutputService): An instance of OutputService.
            screen (Screen): An Asciimatics Screen.
        """
        self._screen = screen
        
    def clear_screen(self):
        """Clears the Asciimatics buffer in preparation for the next rendering.
        
        Args:
            self (OutputService): An instance of OutputService.
        """
        self._screen.clear_buffer(7, 0, 0)
        self._screen.print_at("`" * (constants.MAX_X), 0, 0, 7)
        self._screen.print_at("-" * (constants.MAX_X + constants.PADDLE_LENGTH // 2), 0, constants.MAX_Y, 7)

    def draw_actor(self, actor):
        """Renders the given actor's text on the screen, including
        its color.
        
        Args:
            self (OutputService): An instance of OutputService.
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
        """enders the given list of actors on the screen.
        
        Args:
            self (OutputService): An instance of OutputService.
            actors (list): The actors to render.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    

    def flush_buffer(self):
        """Renders the screen.
        
        Args:
            self (OutputService): An instance of OutputService.
        """
        self._screen.refresh()