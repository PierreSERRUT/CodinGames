#blunder-episode-1
#python

import sys
import math

def upd_pos(d,pos):
    if d == 'EAST':
        n_pos = (pos[0], pos[1] + 1)
    elif d == 'NORTH':
        n_pos = (pos[0] - 1, pos[1])
    elif d == 'WEST':
        n_pos = (pos[0], pos[1] - 1)
    else:
        n_pos = (pos[0] + 1, pos[1])
    return n_pos

cases={}
grid=[]
dir=[]
teleporter=[]

table_dir=['SOUTH', 'EAST', 'NORTH', 'WEST']
table_dir_inv=['WEST', 'NORTH', 'EAST', 'SOUTH']

state_inv = 0
state_drunk = 0
loop=0

direction = 'SOUTH'

l, c = [int(i) for i in input().split()]
for i in range(l):
    row=[]
    row[:0] = input()
    grid.append(row)
    for j in range(c):
        if row[j] == '@' or row[j] == '$':
            cases[row[j]]=(i ,j)
        if row[j] == 'T':
            teleporter.append((i ,j))
    # print(*row,file=sys.stderr, flush=True)

pos = cases['@']
path={pos:0}

while cases['$'] not in path:
    if path[pos]>10:
        loop=1
        break

    val_pos = grid[pos[0]][pos[1]]    
    if val_pos == 'I':
        state_inv = (state_inv+1)%2
    elif val_pos == 'B':
        state_drunk = (state_drunk+1)%2
    elif val_pos == 'S':
        direction = table_dir[0]
    elif val_pos == 'E':
        direction = table_dir[1]
    elif val_pos == 'N':
        direction = table_dir[2]
    elif val_pos == 'W':
        direction = table_dir[3]
    elif val_pos == 'T':
        if pos == teleporter[0]:
            pos = teleporter[1]
        else: pos = teleporter[0]
    
    next_pos = upd_pos(direction, pos)
    val_next_pos = grid[next_pos[0]][next_pos[1]]
    
    c=0
    while val_next_pos == 'X' or val_next_pos == '#': 
        if state_drunk != 0 and val_next_pos == 'X':
            grid[next_pos[0]][next_pos[1]] = ' '
        else:
            if state_inv == 0 :
                direction = table_dir[c%4]
            else:
                direction = table_dir_inv[c%4]
            next_pos=upd_pos(direction, pos)
            c+=1
        val_next_pos = grid[next_pos[0]][next_pos[1]]  

    dir.append(direction)
    pos=next_pos 
    if pos in path.keys():
        path[pos]+=1
    else:
        path[pos]=0

if loop==1:
    print('LOOP')
else:
    for i in dir:
        print(i)