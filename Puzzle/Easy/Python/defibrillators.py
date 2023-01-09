#defibrillators
#python

import sys
import re
from math import sqrt
from math import cos
from math import pi

def dist(lon_a,lat_a,lon_b,lat_b) -> float:
    x=(lon_b-lon_a)* cos((lat_a+lat_b)/2)
    y=lat_b-lat_a
    return (sqrt(x**2+y**2)*6371)

def deg_to_rad(deg) -> float:
    return deg*pi/180

lon = deg_to_rad(float(re.sub(',', '.', input())))
lat = deg_to_rad(float(re.sub(',', '.', input())))
n = int(input())
nomp=''
dist_min=999999
defib=[]
for i in range(n):
    defib.append(input().split(';'))
    for j in range(6):
        defib[i][j]=re.sub(',', '.', defib[i][j])

    tmp=dist(lon,lat,deg_to_rad(float(defib[i][4])),deg_to_rad(float(defib[i][5])))
    if tmp<dist_min:
        dist_min=tmp
        nomp=defib[i][1]

print(nomp)