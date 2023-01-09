#horse-racing-duals
#python

import sys
import math

liste=[]
n = int(input())
for i in range(n):
    liste.append(int(input()))
#print(liste, file=sys.stderr, flush=True)
liste=sorted(liste)
#print(liste, file=sys.stderr, flush=True)

diff_min=10000000
for i in range(n-1):
    t=abs(int(liste[i])-int(liste[i+1]))
    if t<diff_min: diff_min=t

print(diff_min)