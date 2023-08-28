import pygame
from Body import Body, NBody
import math
from Vec import Vec
from Phy import CalculateG

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.font.init()
my_font = pygame.font.SysFont('Mono', 20)
clock = pygame.time.Clock()

pixelScale = 300
body = Body([0, 200, 0], Vec(700, 0), 6380/pixelScale)
body2 = NBody([200, 0, 0], Vec(700 + 6500/pixelScale, 0), 2)
body3 = Body([200, 200, 200], Vec(-580, 0), 1736/pixelScale)
body2.velocity.y = 10.916/300

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
   pointList.append(Vec.ToTuple(Body.PositionInPlane(screen, body2.position)))

   distSQ = pow(body.position.x - body2.position.x, 2) + pow(body.position.y - body2.position.y, 2)
   auth_g = CalculateG(6.6743 * 10**-11, 5.9721 * 10**24, distSQ)

   slope = math.atan2(body2.position.y - body.position.y,body2.position.x - body.position.x)
   g = Vec((auth_g/(pixelScale * 1000)) * math.cos(slope), (auth_g/(pixelScale * 1000)) * math.sin(slope))
   body2.velocity = body2.velocity - g

   pygame.draw.lines(screen, (255, 0, 0), False, pointList)
   pygame.draw.line(screen, (200, 0, 0), Vec.ToTuple(Body.PositionInPlane(screen, body2.position)),Vec.ToTuple(Body.PositionInPlane(screen, body.position)))
   
   text = my_font.render(f'{math.sqrt(distSQ) * pixelScale} Km', False, (255, 0, 0))
   text2 = my_font.render(f'{body2.velocity.Mag() * pixelScale} km/s', False, (255, 0, 0))
   text3 = my_font.render(f'{g.Mag() * (pixelScale * 1000)} m/s2', False, (255, 0, 0))
   text4 = my_font.render(f'{cycle} s', False, (255, 0, 0))

   screen.blit(text, (0,0))
   screen.blit(text2, (0,25))
   screen.blit(text3, (0,50))
   screen.blit(text4, (0,75))

   cycle += 1
   pygame.display.update()
   clock.tick(6000)