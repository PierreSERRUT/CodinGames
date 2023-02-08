#lumen
#python

import sys
import math

n = int(input())
grid = [[0]*n for _ in range(n)]
l = int(input())

for i in range(n):
    line=input().split()
    # print(line, file=sys.stderr, flush=True)

    for j, v in enumerate(line):
        if v=='C': 
            debx = i-l+1 if i-l+1>0 else 0
            deby = j-l+1 if j-l+1>0 else 0
            finx = i+(l*2)//2 if i+(l*2)//2<n else n
            finy = j+(l*2)//2 if j+(l*2)//2<n else n
            for a in range(debx,finx):
                for b in range(deby,finy):
                    grid[a][b]=1

print(sum([l.count(0) for l in grid]))