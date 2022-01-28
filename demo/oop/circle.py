import math


class Circle:
    # Constructor
    def __init__(self, x, y, radius):
        # Object Attributes
        self.x = x
        self.y = y
        self.radius = radius

    # Methods
    def area(self):
        return math.pi * self.radius * self.radius

    @property
    def diameter(self):
        return self.radius * 2


c = Circle(10, 20, 5)  # Create object
print(c.area())
print(c.diameter)  # Property
