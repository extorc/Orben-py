import math
from Vec import Vec
pixelScale = 300

def CalculateG(G, mass, distanceSQ):
    return (G * mass) / (9 * 10 ** 10 * distanceSQ)

def PhyUpdate(body, body2, body_mass):
   distSQ = pow(body.position.x - body2.position.x, 2) + pow(body.position.y - body2.position.y, 2)
   auth_g = CalculateG(6.6743 * 10**-11, body_mass, distSQ)
   slope = math.atan2(body2.position.y - body.position.y,body2.position.x - body.position.x)
   return Vec((auth_g/(pixelScale * 1000)) * math.cos(slope), (auth_g/(pixelScale * 1000)) * math.sin(slope)), distSQ