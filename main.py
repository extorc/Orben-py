import pygame
from Body import Body, NBody
import math
from Vec import Vec
from Phy import CalculateG

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.font.init()
my_font = pygame.font.SysFont('Mono', 20)
clock = pygame.time.Clock()

body = Body([0, 200, 0], Vec(700, 0), 31.9)
body2 = NBody([200, 0, 0], Vec(732.9, 0), 2)
body2.velocity.y = 5.458/100

active = True
cycle = 0
pointList = [Vec.ToTuple(Body.PositionInPlane(screen, Vec(732.9, 0)))]

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False

   body2.position = body2.position + body2.velocity

   screen.fill([20, 20, 20])
   body.Draw(screen)
   body2.Draw(screen)
   pointList.append(Vec.ToTuple(Body.PositionInPlane(screen, body2.position)))

   distSQ = pow(body.position.x - body2.position.x, 2) + pow(body.position.y - body2.position.y, 2)
   auth_g = CalculateG(6.6743 * 10**-11, 5.9721 * 10**24, distSQ)
   norm_g = auth_g/200000

   slope = math.atan2(body2.position.y - body.position.y,body2.position.x - body.position.x)
   g = Vec(norm_g * math.cos(slope), norm_g * math.sin(slope))
   body2.velocity = body2.velocity - g

   pygame.draw.lines(screen, (255, 0, 0), False, pointList)
   pygame.draw.line(screen, (200, 0, 0), Vec.ToTuple(Body.PositionInPlane(screen, body2.position)),Vec.ToTuple(Body.PositionInPlane(screen, body.position)))
   
   text = my_font.render(f'{math.sqrt(distSQ) * 200} Km', False, (255, 0, 0))
   text2 = my_font.render(f'{body2.velocity.Mag() * 200} km/s', False, (255, 0, 0))
   text3 = my_font.render(f'{g.Mag() * 200000} m/s2', False, (255, 0, 0))
   text4 = my_font.render(f'{cycle} s', False, (255, 0, 0))

   screen.blit(text, (0,0))
   screen.blit(text2, (0,25))
   screen.blit(text3, (0,50))
   screen.blit(text4, (0,75))

   cycle += 1
   pygame.display.update()
   clock.tick(6000)