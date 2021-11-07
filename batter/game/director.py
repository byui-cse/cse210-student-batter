"""Module director containing class Director and its corresponding
methods.It is used to control the sequence of play.
"""
from time import sleep
from typing import final
from game import constants, handle_collisions_action
from game.actor import Actor
from game.point import Point
from game.score import Score

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        self (Director): An instance of Director.
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
        keep_playing(Director): Whether the game continue or not
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
        """Starts the game loop to control the sequence of play.
            Args:
                self: An instance of start game
            Attributes:
                while(loop): controls the sequence of play
                fianl_score: displays score
                number_of_bricks: display bricks


        """
        
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            self._keep_playing = self._script["update"][1].checkPlay()
            sleep(constants.FRAME_LENGTH)

        
        final_score = self._cast["score"][0]._points
        number_of_bricks = self._cast["brick"]
        self._cast = {} 

        if len(number_of_bricks):
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
                        
        else:
            _final_Text = Actor()
            _final_Text.set_color("yellow")
            _final_Text.set_text(
                "\t\t\tYou Won!.\n\n\t\t\t Your final score is: " + str(final_score))
            x = int((constants.MAX_X * 2/3) - len(_final_Text.get_text()))
            y = (constants.MAX_Y // 2) - 1
            position = Point(x, y)
            _final_Text.set_position(position)

            self._cast["final_Text"] = [_final_Text]
            self._cue_action("output")

        sleep(constants.FINAL_MESSAGES_LAPSE_TIME)  # final delay
        _final_Text.set_text(
            "\t\t\tThanks for playing Batter with Team2.\n\n\t\t\tTry again whenever you are ready.")
        self._cue_action("output")
        sleep(constants.FINAL_MESSAGES_LAPSE_TIME)

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)