""" 
"""
from time import sleep
from typing import final
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
        
     
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        #main loop of the game
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            self._keep_playing = self._script["update"][1].checkPlay()
            sleep(constants.FRAME_LENGTH)

        #messages at the end
        final_score = self._cast["score"][0]._points
        self._cast = {} 

        _final_Text = Actor()
        _final_Text.set_color("green")
        _final_Text.set_text(
            "\t\t\tGAME OVER.\n\n\t\t\t Your final score is: " + str(final_score))
        x = int((constants.MAX_X * 2/3) - len(_final_Text.get_text()))
        y = (constants.MAX_Y  // 2) - 1
        position = Point(x, y)
        _final_Text.set_position(position)

        self._cast["final_Text"] = [_final_Text]
     
        self._cue_action("output")
        sleep(constants.FINAL_MESSAGES_LAPSE_TIME) # final delay
        _final_Text.set_text("\t\t\tThanks for playing Batter with Team2.\n\n\t\t\tTry again whenever you are ready.")
        self._cue_action("output")
        sleep(constants.FINAL_MESSAGES_LAPSE_TIME)


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)
