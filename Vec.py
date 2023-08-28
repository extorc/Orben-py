import math

class Vec:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, v2):
        return Vec(self.x + v2.x, self.y + v2.y)
    
    def __sub__(self, v2):
        return Vec(self.x - v2.x, self.y - v2.y)
    
    def Mag(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    @staticmethod
    def ToTuple(x):
        return (x.x, x.y)