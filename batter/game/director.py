""" 
"""
from time import sleep
from game import constants, handle_collisions_action
from game.actor import Actor
from game.point import Point

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._keep_playing = True
        #self._final_Text = "Game over."
        
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            self._keep_playing = self._script["update"][1].checkPlay()
            sleep(constants.FRAME_LENGTH)

        
        self._cast = {} 

        x = int((constants.MAX_X / 2) - 5)
        y = int((constants.MAX_Y  / 2) - 1)
        position = Point(x, y)
        _final_Text = Actor()

        _final_Text.set_text("Game Over")
        _final_Text.set_position(position)

        self._cast["final_Text"] = [_final_Text]

        self._cue_action("output") 
        sleep(5) # final delay


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)