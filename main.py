import pygame
from Body import Body, NBody
import math
from Vec import Vec
from Phy import pixelScale, PhyUpdate
from Font import RenderText

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.font.init()
my_font = pygame.font.SysFont('Mono', 20)

body = Body([0, 200, 0], Vec(700, 0), 6380/pixelScale)
body2 = NBody([200, 0, 0], Vec(700 + 6500/pixelScale, 0), 2)
body3 = Body([200, 200, 200], Vec(-580, 0), 1736/pixelScale)
body2.velocity.y = 10.966/300

active = True
cycle = 0
pointList = [Vec.ToTuple(Body.PositionInPlane(screen, Vec(700 + 6500/pixelScale, 0)))]

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False

   body2.position = body2.position + body2.velocity

   screen.fill([20, 20, 20])
   body.Draw(screen)
   body2.Draw(screen)
   body3.Draw(screen)

   if cycle % 500 == 0:
      pointList.append(Vec.ToTuple(Body.PositionInPlane(screen, body2.position)))

   g ,distSQ   = PhyUpdate(body, body2, 5.9721 * 10**24)
   g2,distSQ2  = PhyUpdate(body3, body2, 7.3476 * 10**22)
   body2.velocity = body2.velocity - (g+g2)

   pygame.draw.lines(screen, (255, 0, 0), False, pointList)
   pygame.draw.line(screen, (200, 0, 0), Vec.ToTuple(Body.PositionInPlane(screen, body2.position)),Vec.ToTuple(Body.PositionInPlane(screen, body.position)))
   
   RenderText(my_font, screen, f'{math.sqrt(distSQ) * pixelScale} Km', 0)
   RenderText(my_font, screen, f'{math.sqrt(distSQ2) * pixelScale} Km', 1)
   RenderText(my_font, screen, f'{body2.velocity.Mag() * pixelScale} km/s', 2)
   RenderText(my_font, screen, f'{(g + g2).Mag() * (pixelScale * 1000)} m/s2', 3)
   RenderText(my_font, screen, f'{cycle}', 4)

   cycle += 1
   pygame.display.update()