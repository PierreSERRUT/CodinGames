#shoot-enemy-aircraft
#python

import sys
import math

n = int(input())
grid=[]
rockets=[]

for i in range(n):
    grid.append(input())

launcher=grid[-1].index('^')
    
for i in range(n-1):
    for j in range(len(grid[i])):
        if grid[i][j]=='>' or grid[i][j]=='<' :
            rockets.append(abs(j-launcher)-(n-i))
    
for i in range(max(rockets)+1):
    if i in rockets:
        print("SHOOT")
    else:
        print("WAIT")