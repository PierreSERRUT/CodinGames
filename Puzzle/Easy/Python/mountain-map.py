#mountain-map
#python


import sys
import math

heights=[]
mountains=[]

n = int(input())
for i in input().split():
    heights.append(int(i))

h_max=max(heights)
res=['']*h_max

for i in range(n):
    mountains.append(['']*h_max)
    print(mountains[i], file=sys.stderr, flush=True)

for ind, val in enumerate(heights):
    print(f'ind:{ind}, val:{val}', file=sys.stderr, flush=True)
    c=1
    for i in range(h_max-1,-1,-1):
        if val-1 < i:
            mountains[ind][i]+=' '*val*2
        elif val-1 >= i:
            mountains[ind][i]+=' '*(val-c)+'/'+' '*((c-1)*2)+'\\'+' '*(val-c)
            c+=1

for i in range(h_max-1,-1,-1):
    max_ind=0
    for k in range(n):
        res[i]+=mountains[k][i]
    for ind,val in enumerate(res[i]):
        if val != ' ':
            max_ind=ind
    res[i]=res[i][:max_ind+1]
    print(res[i])