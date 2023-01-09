#shadows-of-the-knight-episode-1
#python

import sys
from math import trunc
from math import floor

class pos:
    def __init__(self,w,h):
        self.w=w
        self.h=h

def diff(x1,x2):
    return abs(x1-x2)

def Debug(var_name,v):
    print(var_name,v, file=sys.stderr, flush=True)

w, h = [int(i) for i in input().split()]
build=pos(w,h)

n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
p0=pos(x0,y0)
pl=pos(0,0)
pmin=pos(0,0)
pmax=pos(build.w,build.h)

while True:
    bdir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    dw=dh=0
    if 'R' in bdir:
        #UR,R,DR
        pl.w=p0.w
        if p0.w > pmin.w:   pmin.w=p0.w
        dw=round((pmax.w-pl.w)/2)
        if dw<1:  dw=1
    elif 'L' in bdir:
        #UL,L,DL
        pl.w=p0.w
        if p0.w < pmax.w:   pmax.w=p0.w
        dw=floor((pmin.w-pl.w)/2)
        if dw>-1:  dw=-1

    if 'U' in bdir:
        #U,UR,UL
        pl.h=p0.h
        if p0.h < pmax.h:   pmax.h=p0.h
        dh=floor((pmin.h-pl.h)/2)
        if dh>-1:  dh=-1
    elif 'D' in bdir:
        #D,DR,DL
        pl.h=p0.h
        if p0.h > pmin.h:   pmin.h=p0.h
        dh=round((pmax.h-pl.h)/2)
        if dh<1:  dh=1
    cible=pos(int(p0.w+dw),int(p0.h+dh))
    p0=cible
    print(str(cible.w)+' '+str(cible.h))
