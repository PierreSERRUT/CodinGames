#the-fall-episode-1
#python

import sys
import math

map_S = { 1:['LB', 'TB', 'RB'], 2:['LR', 'RL'], 3:['TB'], 4:['TL', 'RB'], 5:['LB', 'TR'], 6:['LR', 'RL'], 7:['TB', 'RB'], 8:['LB', 'RB'], 9:['LB', 'TB'], 10:['TL'], 11:['TR'], 12:['RB'], 13:['LB'] }
map_F = { 4:'L', 5:'R', 6:'T', 10:'L', 11:'R' }
# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
grid=[]
for i in range(h):
    grid.append(input().split(' '))

ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

while True:
    direct=''

    inputs = input().split()
    xi = int(inputs[0])
    yi = int(inputs[1])
    pos = inputs[2]

    num=int(grid[yi][xi])
    #print(xi,yi,':',num,file=sys.stderr, flush=True)
    if num in map_S:
        for i in map_S[num]:
            if i[0] == pos[0]:
                direct=i[1]
                #print('pos:',pos,'map_S[',num,']:',i,'direct:',direct,file=sys.stderr, flush=True)
    if direct == 'B':   yi+=1
    elif direct == 'L': xi-=1
    elif direct == 'R': xi+=1
    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print(str(xi)+' '+str(yi))
