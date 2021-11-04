from game.action import Action

class DrawActorsAction(Action):
    """
    A code template for drawing actors. The responsibility of this class of
    objects is use an output service to draw all actors on the screen.
    
    Stereotype:
        Controller
        
    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self,output_service):
        '''
        A code template for drawing actors. The responsibility of this
        class of objects is translate user input into some kind of intent.
        
        Stereotype:
            Controller

        Attributes:
            _output_service (OutputService): An instance of OutputService.
        '''
        self._ouput_service = output_service

    def execute(self, cast):
        '''
        Executes the drawing using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        '''
        self._output_service.clear_screen()
        for group in cast.values():
            self._output_service.draw_actors(group)
        self._output_service.flush_buffer()