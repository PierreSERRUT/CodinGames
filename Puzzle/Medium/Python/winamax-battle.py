#winamax-battle
#python

import sys
import math

def val_card(p):
    if p == 'J': return 11
    elif p == 'Q': return 12
    elif p == 'K': return 13
    elif p == 'A': return 14
    elif p == '1': return 10
    else: return int(p)

def p1w(c1,c2):
    c1.append(c1[0])
    c1.append(c2[0])
    c1.pop(0)
    c2.pop(0)

def p2w(c1,c2):
    c2.append(c1[0])
    c2.append(c2[0])
    c1.pop(0)
    c2.pop(0)

def battle(c1,c2):
    q1=[]
    q2=[]
    w=0
    while w==0:
        for i in range(4):
            q1.append(c1[0])
            q2.append(c2[0])
            c1.pop(0)
            c2.pop(0)
            l1=len(c1)
            l2=len(c2)
            if l1 == 0 or l2 == 0:
                return 1
        if c1[0] > c2[0]:
            w=1
            for i in range(len(q1)):
                c1.append(q1[i])
            c1.append(c1[0])
            for i in range(len(q2)):
                c1.append(q2[i])
            c1.append(c2[0])
            c1.pop(0)
            c2.pop(0)
        elif c1[0] < c2[0]:
            w=1
            for i in range(len(q1)):
                c2.append(q1[i])
            c2.append(c1[0])
            for i in range(len(q2)):
                c2.append(q2[i])
            c2.append(c2[0])
            c1.pop(0)
            c2.pop(0)

cards_1=[]
cards_2=[]

n = int(input())  # the number of cards for player 1
for i in range(n):
    c=input()
    cards_1.append(val_card(c[0]))  # the n cards of player 1

m = int(input())  # the number of cards for player 2
for i in range(m):
    c=input()
    cards_2.append(val_card(c[0]))  # the m cards of player 2
print(cards_1, file=sys.stderr, flush=True)
print(cards_2, file=sys.stderr, flush=True)
print(file=sys.stderr, flush=True)
bat=0
tie=0
nb_coup=0
queue1=[]
queue2=[]
while n > 0 and m > 0:
    #print(cards_1, file=sys.stderr, flush=True)
    #print(cards_2, file=sys.stderr, flush=True)
    
    nb_coup+=1
    p1=cards_1[0]
    p2=cards_2[0]
       
    if p1 > p2:     p1w(cards_1,cards_2)
    elif p1 < p2:   p2w(cards_1,cards_2)
    elif p1 == p2:  tie=battle(cards_1,cards_2)
        
    n=len(cards_1)
    m=len(cards_2)
    print(file=sys.stderr, flush=True)
    print(n,m,file=sys.stderr, flush=True)
    if tie==1:
        s="PAT"
        break
    elif n > m: s="1 "+str(nb_coup)
    else:       s="2 "+str(nb_coup)

print(s)
