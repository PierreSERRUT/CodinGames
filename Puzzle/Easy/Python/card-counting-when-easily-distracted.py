#card-counting-when-easily-distracted
#python3

import sys
import math

sc=input().split('.')
bt = int(input())

c=[4,4,4,4,4,4,4,4,4,16]
nbt=0
tot_cards=52
valid=[]
d={'K':10,'Q':10,'J':10,'T':10,'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}


for i in sc:
    v=1
    for j in range(len(i)):
        if i[j] not in d:       
            v=0
    valid.append(v)
#print('valid:',valid, file=sys.stderr, flush=True)

for i in range(len(sc)):
    if valid[i]==1:
        for j in range(len(sc[i])):
            tot_cards-=1
            c[d[sc[i][j]]-1]-=1

for i in range(10):
    if i+1<bt: 
        nbt=nbt+c[i]
p=round(nbt/tot_cards*100)
print(f'{p}%')
