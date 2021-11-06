from game.move_actors_action import MoveActorsAction

class MovePlayerAction(MoveActorsAction):

    def execute(self, cast):
        for pad in cast.paddle_parts:
            if not pad.get_velocity().is_zero():
                self._move_actor(pad)
            