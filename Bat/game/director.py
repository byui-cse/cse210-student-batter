from time import sleep
from game import constants, input_service
from game.brick import Brick
from game.score import Score
from game.bat import Bat
from game.ball import Ball
from game.point import Point

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        food (Food): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        snake (Snake): The player or snake.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.bricks = []
        self.broken_bricks = ''
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._bat = Bat()
        self._ball = Ball()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        y = 1
        for row in range(4):
            for col in range(constants.MAX_X):
                brick = Brick(col,y)
                self.bricks.append(brick)
            y +=1
        
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)


    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        self._bat.right_or_left(self._input_service.get_direction())
        self._ball.wall_bounce()
        self.broken_bricks = self._ball.ball_collision(self.bricks)
        
        if self._ball.get_position() == self._bat.get_position():
            self._ball.bounce()
        



    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self._bat.move_next()
        self._ball.move_next()
        
        for i in self.bricks:
            if i == self.broken_bricks:
                self.bricks.remove(i)
                self._score.add_points(i.get_points())
        
        if self._bat.bat_collision(self._ball):
            self._ball.bounce()
        
        if self._ball.missed():
            self._keep_playing = False
        
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        
        for i in self.bricks:
            self._output_service.draw_actor(i)
                
        
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actor(self._bat)
        self._output_service.draw_actor(self._ball)
        self._output_service.flush_buffer()