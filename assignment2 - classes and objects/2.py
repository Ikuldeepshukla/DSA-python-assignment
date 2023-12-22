# Define a class Circle with instance object variable radius. Provide getter and setter for radius. Also define getArea and getCircumference() methods.

import math
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def setRadius(self, newRadius):
        self.radius = newRadius

    def getRadius(self):
        return self.radius
    
    def getArea(self):
        return math.pi * self.radius * self.radius
    
    def getCircumference(self):
        return 2 * math.pi * self.radius
    
# creating class object
c1 = Circle(5)
print('Circle 1 Radius', c1.getRadius())
print('Circle 1 Area', c1.getArea())
print('Circle 1 Circumference', c1.getCircumference())
c1.setRadius(8);
print('Circle 1 updated Radius', c1.getRadius())
