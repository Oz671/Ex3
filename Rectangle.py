class Rectangle:
    def __init__(self, height, width):
        self.h = height
        self.w = width
    def perim(self):
        return (2 * self.h) + (2 * self.w)
    def area(self):
        return self.h * self.w
    def isSquare(self):
        return (self.h == self.w)
    
x = Rectangle(3,5)
print (x.perim())
print (x.area())
print (x.isSquare())

y = Rectangle(3,3)
print (y.perim())
print (y.area())
print (y.isSquare())