#mars-lander-episode-1
#python

import sys
import math

import sys
import math

GRAVITE=3.711 

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class lander:
    def __init__(self,x,y,hspeed,vspeed,fuel,angle,power):
        self.x=x
        self.y=y
        self.hspeed=hspeed
        self.vspeed=vspeed
        self.fuel=fuel
        self.angle=angle
        self.power=power

def Debug(var_name, var):
    print(var_name, var, file=sys.stderr, flush=True)

land=[]
area=[] 

output=""

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    land.append(point(land_x,land_y))

while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    rover=lander(x,y,h_speed,v_speed,fuel,rotate,power)
    if rover.vspeed < -39:
        print('0 4')
    else: print('0 0')