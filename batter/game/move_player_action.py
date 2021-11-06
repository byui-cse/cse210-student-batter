from game.action import Action
from game.point import Point
from game import constants

class MovePlayerAction(Action):

    def execute(self, cast):
        if not cast.paddle_parts[0].get_velocity().is_zero():
                self._move_connected_actor_x(cast.paddle_parts)
        
    def _move_connected_actor_x(self, actor_parts):
        anchor_actor = actor_parts[0]
        velocity = anchor_actor.get_velocity()
        x2 = velocity.get_x()
        position = anchor_actor.get_position()
        x1 = position.get_x()
        y = position.get_y()
        for offset, actor in enumerate(actor_parts):
            x = x1 + x2 + offset
            if x >= constants.MAX_X - 1 + offset:
                x = constants.MAX_X - 1 + offset
            elif x <= 1 + offset:
                x = 1 + offset
            position = Point(x, y)
            actor.set_position(position)