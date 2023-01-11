#network-cabling
#python

import sys
import math
import bisect

def dist(x1,x2,y1,y2):
    return abs(x2-x1)+abs(y2-y1)

homes=[]
xs=[]
ys=[]
n = int(input())
print('n:',n,file=sys.stderr, flush=True)

for i in range(n):
    x, y = [int(j) for j in input().split()]
    bisect.insort(xs,x)
    bisect.insort(ys,y)
    homes.append([x,y])
#print('xs:',xs,file=sys.stderr, flush=True)
#print('ys:',ys,file=sys.stderr, flush=True)

if n==1:        med=1
elif n%2==1:    med=int((n+1)/2)
else:           med=int(n/2) # et n/2+1

y_central=ys[med-1]
print('y_central:',y_central,file=sys.stderr, flush=True)

d=dist(xs[0],xs[n-1],0,0)
print(' initial d:',d,file=sys.stderr, flush=True)
for i in range(n):
    tmp=dist(0,0,homes[i][1],y_central)
    d+=tmp
    #print('tmp:',tmp,'d:',d,file=sys.stderr, flush=True)
print(d)