from math import pi

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    """
    Holds data on a circle in the plane
    """
    def __init__(self, a, b, c=None):
        if c is None:
            # Circle(Point, scalar)
            self.center = a
            self.r = b
        else:
            # Circle(scalar, scalar, scalar)
            self.center = Point(a, b)
            self.r = c

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, new_r):
        assert new_r > 0
        self._r = new_r

    def __mul__(self, scale_by):
        return Circle(self.center, self.r * scale_by)

    __rmul__ = __mul__

    def area(self):
        return pi * self.r**2

    def circumference(self):
        return 2 * pi * self.r

    def move(self, new_center):
        self.center = new_center