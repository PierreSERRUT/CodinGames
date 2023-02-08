#ghost-legs
#python

import sys
import math

lines=[]
w, h = [int(i) for i in input().split()]
for i in range(h):
    lines.append(input())
    #print(lines[i],file=sys.stderr, flush=True)

inp=lines[0].split()
for z in range(len(inp)):
    s=inp[z]
    index=z*3
    #print(s,z,index,file=sys.stderr, flush=True)
    for i in range(1,h-1):
        n_ind=index
        if index>0:
            if lines[i][index-1]=='-':
                n_ind=index-3 
        if index<w-1:
            if lines[i][index+1]=='-':
                n_ind=index+3 
        index=n_ind
    s+=lines[h-1][index]
    print(s)