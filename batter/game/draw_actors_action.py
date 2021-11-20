#origin code from rfk This will need to change slightly too
from game.action import Action

# TODO: Define the DrawActorsAction class here
# this working code comes from the teachers answers
class DrawActorsAction(Action):
    """A code template for drawing actors. The responsibility of this calss of objects
    is is to use an output service to draw all actors on the screen.
     
     Stereotype : Controller
     
     Atrributes: _output_service (OutputService):  An instance of OutputService.
     
     """
    def __init__(self, output_service):
        """The class constructor. 
        
        Args: output_service (OutputService): An instance of OutputService.
        
        """
        self._output_service = output_service
        
    def execute(self, cast):
        """ Executes the action using the given actors. 
        Args: cast(dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()
        for group in cast.values():
            self._output_service.draw_actors(group)
        self._output_service.flush_buffer()