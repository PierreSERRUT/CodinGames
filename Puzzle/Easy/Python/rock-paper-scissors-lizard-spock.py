#rock-paper-scissors-lizard-spock
#python

import sys
import math

def battle(d, id_a, id_b):
    a=d[id_a]
    b=d[id_b]
    if a == 'R':
        if b == 'L' or b == 'C':
            return id_a
        elif b == 'P' or b == 'S':
            return id_b
    elif a == 'C':
        if b == 'P' or b == 'L':
            return id_a
        elif b == 'S' or b == 'R':
            return id_b
    elif a == 'P':
        if b == 'R' or b == 'S':
            return id_a
        elif b == 'L' or b == 'C':
            return id_b
    elif a == 'L':
        if b == 'S' or b == 'P':
            return id_a
        elif b == 'R' or b == 'C':
            return id_b
    elif a == 'S':
        if b == 'C' or b == 'R':
            return id_a
        elif b == 'P' or b == 'L':
            return id_b   
    return min(id_a,id_b)

player={}
path={}
n = int(input())
turn=[]
for i in range(n):
    inputs = input().split()
    id_p=int(inputs[0])
    player[id_p]=inputs[1]
    turn.append(id_p)
#print('player:',player, file=sys.stderr, flush=True)

l=len(turn)
while l > 1:
    #print('turn:',turn, file=sys.stderr, flush=True)
    next_turn = []
    for i in range(l//2):
        a=turn.pop()
        b=turn.pop()
        res=battle(player, a, b)
        print(f'a ({a}) vs b ({b}) : {res} ', file=sys.stderr, flush=True)
        next_turn.append(res)
        if res not in path:
            path[res]=[]
        if res==a:
            path[res].append(b)
        else:
            path[res].append(a)
    turn = next_turn
    l = len(turn)

print(*turn)
print(*path[turn[0]])