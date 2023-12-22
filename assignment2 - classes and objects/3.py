# Define a class Rectangle with length and breadth as instance object variables. Provide setDimentions(), showDimentions() and getArea() method in it.

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def setDimentions(self, updatedHeight, updatedWidth):
        self.height = updatedHeight
        self.width = updatedWidth
    
    def showDimentions(self):
        print('Dimentions: Height-', self.height, ',Width-', self.width)
    
    def getArea(self):
        return self.height * self.width
    
# object initialization
r1 = Rectangle(10, 30)
r1.showDimentions()
print('Area:', r1.getArea())
r1.setDimentions(30, 60)
print('Updated')
r1.showDimentions()
print('Area after dientions update', r1.getArea())

