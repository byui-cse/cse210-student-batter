from game.action import Action

class DrawActorsAction(Action):
    """
        Draws the actors to the screen. 

        This is a controller class
    
        Takes in output_services
    """
    def __init__(self, output_service):
        """
            class instructor

            takes an instance of output_services
        """
        self._output_service = output_service

    def execute(self, cast):
        """
            Executes the action of the actors

            takes in the cast dictionary. Game actors {key: tag, value: list}
        """
        self._output_service.clear_screen()
        for group in cast.values():
            self._output_service.draw_actors(group)
        self._output_service.flush_buffer()