from math import sin, cos, tan, atan, radians, degrees, sqrt, pi

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.t = degrees(atan(x / y) + (pi if x>=0 else 0))
        self.r = sqrt(x**2 + y**2)

    @classmethod
    def from_polar(cls, t, r):
        x = sin(radians(t)) * r
        y = cos(radians(t)) * r
        return Vector(x, y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
