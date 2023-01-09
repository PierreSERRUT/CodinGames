#ascii-art
#python

import sys
import math
import string

class intervalle:
    def __init__(self,x1,x2):
        self.x1=x1
        self.x2=x2

l = int(input())
h = int(input())
t = input()
#print(t, file=sys.stderr, flush=True)
r=[]

for i in range(h):
    r.append(input())

interv=[]
k=0
for j in range(h):
    sortie=''
    for i in t:
        temp=ord(i)
        if temp>64 and temp<91:
            temp=(temp-65)*l
        elif temp>96 and temp<123:
            temp=(temp-97)*l
        else:
            temp=26*l
        interv.append(intervalle(temp,temp+l))
        sortie=sortie+(r[j][interv[k].x1:interv[k].x2])
        k+=1
    print(sortie)