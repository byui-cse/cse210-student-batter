""" 
"""
import random
class Point:
    """Represents distance from an origin (0, 0).

    Stereotype:
        Information Holder

    Attributes:
        _x (integer): The horizontal distance.
        _y (Point): The vertical distance.
    """
    
    def __init__(self, x, y):
        """The class constructor.
        
        Args:
            x (integer): A horizontal distance.
            y (integer): A vertical distance.
        """
        self._x = x
        self._y = y

    def add(self, other):
        """Gets a new point that is the sum of this and the given one.

        Args:
            other (Point): The Point to add.

        Returns:
            Point: A new Point that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        """Whether or not this Point is equal to the given one.

        Args:
            other (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        """Gets the horizontal distance.
        
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.
        
        Returns:
            integer: The vertical distance.
        """
        return self._y

    def is_zero(self):
        """Whether or not the point is zero or x is equal to 0 and y is equal to 0.
        
        Returns:
            boolean: True if x is equal to  0 and y is equal to 0; false if otherwise.
        """
        return self._x == 0 and self._y == 0

    def random_velocity_generator(self):
        """Give a random x value to horizontal velocity (self._x)
        
        Args:
            self (Point): A point

        Returns:
            Point: A point with a random x value. 
        """
        if self._x > 0:
            x = random.randint(0, 2)
        elif self._x < 0:
            x = random.randint(-2, 0)
        else:
            x = random.randint(-2, 2)
        y = self._y
        return Point(x, y)
                
    def reverse(self):
        """Gets a new Point that is the reverse of this one.
        
        Returns:
            Point: A new Point that is reversed.
        """
        x = self._x * -1
        y = self._y * -1
        return Point(x, y)

    def reverse_y(self):
        """Gets a new y Point that is the reverse of this one.
        
        Returns:
            Point: A new y Point that is reversed.
        """
        x = self._x
        y = self._y * -1
        return Point(x, y)

    def reverse_x(self):
        """Gets a new y Point that is the reverse of this one.
        
        Returns:
            Point: A new y Point that is reversed.
        """
        x = self._x * -1
        y = self._y
        return Point(x, y)  