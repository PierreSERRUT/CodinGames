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
            false=1
            break
        row.append(n)
    grid.append(row)
    print(grid[i],file=sys.stderr, flush=True)
if false!=1:
    try:
        for i in range(9):
            col=[]
            for j in range(9):
                n=grid[j][i]
                if n in col:
                    false=1
                    break
                col.append(n)
    except:
        print('err col',file=sys.stderr, flush=True)
if false!=1:
    try:
        for i in range(1,4):
            for j in range(1,4):
                subgrid=[]
                for k in range(3):
                    for l in range(3):
                        n=grid[k+3*(i-1)][l+3*(j-1)]
                        if n in subgrid:
                            false=1
                            break
                        subgrid.append(n)
    except:
        print('err subgrid',file=sys.stderr, flush=True)
if false==1:
    print('false')
else:
    print('true')