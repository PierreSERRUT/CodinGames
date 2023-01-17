#power-of-thor-episode-1
#python

import sys
import math

def update_pos(dir, val):
    if dir == "N":
        return val - 1
    elif dir == "S":
        return val + 1
    elif dir == "E":
        return val + 1
    elif dir == "W":
        return val - 1


light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

tx=ty=delta=delta_x=delta_y=0
tx=initial_tx
ty=initial_ty

while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    dest=""
    destX=""
    destY=""
    delta_x=light_x - tx
    delta_y=light_y - ty

    if delta_y > 0: 
        destY+="S"
    elif delta_y < 0:
        destY+="N"
        
    if delta_x > 0 : 
        destX+="E"
    elif delta_x < 0 :
        destX+="W"
      
    delta=abs(delta_x) - abs(delta_y)
    if delta > 0 : 
        dest=destX
        tx=update_pos (destX, tx)
    elif delta < 0:
        dest=destY
        ty=update_pos(destY,ty)
    else:
        tx=update_pos(destX,tx)
        ty=update_pos(destY,ty)
        dest = destY + destX
    
    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(dest)
