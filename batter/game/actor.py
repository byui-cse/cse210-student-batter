from game.point import Point

class Actor:
    """A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position
    and velocity in 2d space.

    Stereotype:
        Information Holder

    Attributes:
        _points (number): The actor's points.
        _text (string): The textual representation of the actor.
        _position (Point): The actor's position in 2d space.
        _velocity (Point): The actor's speed and direction.
    """

    def __init__(self):
        """The class constructor."""
        self._points = 0
        self._text = ""
        self._tag = ""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    

    def get_position(self):
        """Gets the actor's position in 2d space.

        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position

    def get_text(self):
        """Gets the actor's textual representation.

        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.

        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    def set_position(self, position):
        """Updates the actor's position to the given one.

        Args:
            position (Point): The given position.
        """
        self._position = position

    def set_text(self, text):
        """Updates the actor's text to the given value.

        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.

        Args:
            position (Point): The given velocity.
        """
        self._velocity = velocity

    def set_tag(self, text):
        """Updates the tag of our dictionary items.

        Args:
            text ([str]): The string to set the tag to.
        """

        self._tag = text
    
    def get_points(self):
        """Gets the actor's point value.
        
        Returns:
            integer: The actor's point value.
        """
        return self._points 
    
    def set_points(self, points):
        """Updates the actor's points to the given value.
        
        Args:
            integer (integer): The given value.
        """
        self._points = points  

    def add_points(self, points):

        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Score): An instance of Score.
            points (integer): The points to add.
        """

        self._points += points