#sudoku-validator
#python

import sys
import math

false=0
grid=[]
for i in range(9):
    row=[]
    for j in input().split():
        n=int(j)
        if n in row:
            print('false') 
            exit()
        row.append(n)
    grid.append(row)

for i in range(9):
    col=[]
    for j in range(9):
        n=grid[j][i]
        if n in col:
            print('false') 
            exit()
        col.append(n)

for i in range(1,4):
    for j in range(1,4):
        subgrid=[]
        for k in range(3):
            for l in range(3):
                n=grid[k+3*(i-1)][l+3*(j-1)]
                if n in subgrid:
                    print('false') 
                    exit()
                subgrid.append(n)
                
print('true')