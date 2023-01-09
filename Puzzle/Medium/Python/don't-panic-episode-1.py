#don't-panic-episode-1
#python

import sys
import math

def Debug(var_name):
    print(var_name, file=sys.stderr, flush=True)

class clone:
    def __init__(self,floor,pos,direction):
        self.floor=floor
        self.pos=pos
        self.dir=direction

class pos:
    def __init__(self, floor, pos):
        self.floor=floor
        self.pos=pos

asc=[]

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
sortie=pos(exit_floor,exit_pos)
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    asc.append(pos(elevator_floor, elevator_pos))
    
s="WAIT"
# game loop
while True:
    inputs = input().split()
    lead=clone(int(inputs[0]), int(inputs[1]), inputs[2])
    direct=''
    s="WAIT"
    if sortie.floor == lead.floor:
        direct='exit'
    else:
        direct='asce'
    #Debug(direct)
    #Debug("lead.pos:")
    #Debug(lead.pos)
    #Debug("lead.floor:")
    #Debug(lead.floor)
    #Debug("lead.dir:")
    #Debug(lead.dir)
    if (direct=='exit' and ((sortie.pos>lead.pos and lead.dir=="LEFT") or (sortie.pos<lead.pos and lead.dir=="RIGHT"))):
        s="BLOCK"
    elif nb_elevators >0:
        for i in range(nb_elevators):
            if asc[i].floor == lead.floor:
                if (direct=='asce' and ((asc[i].pos>lead.pos and lead.dir=="LEFT") or (asc[i].pos<lead.pos and lead.dir=="RIGHT"))):
                    s="BLOCK"
    # action: WAIT or BLOCK
    print(s)
