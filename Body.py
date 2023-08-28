import pygame
from Vec import Vec

class Body:
    def __init__(self, color, position, radius):
        self.color = color
        self.position = position
        self.radius = radius
    
    def Draw(self, screen):
        pygame.draw.circle(screen, self.color,Vec.ToTuple(Body.PositionInPlane(screen, self.position)),self.radius)

    @staticmethod
    def PositionInPlane(screen, position):
        return Vec(position.x+screen.get_width()/2, -position.y+screen.get_height()/2)
    
class NBody(Body):
    def __init__(self, color, position, radius):
        super().__init__(color, position, radius)
        self.velocity = Vec(0, 0)