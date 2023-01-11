#the-gift
#python

import sys
import math
import bisect

n = int(input())
c = int(input())
b_tot=0
bud=[]
opt=[]
for i in range(n):
    b = int(input())
    b_tot+=b
    bisect.insort(bud,b)

m=c//n

if c>b_tot:
    print("IMPOSSIBLE")
else: 
    for i in range(len(bud)):
        if bud[i] < m:
            opt.append(bud[i])
            c-=bud[i]
            n-=1
            m=c//n
        else:
            opt.append(m)
            c-=m
            if c!=0:
                n-=1
                m=c//n
        print(opt[i])