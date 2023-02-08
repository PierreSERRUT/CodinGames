#logic-gates
#python

import sys
import math

def logic(op,x,y):
    s=''
    for i in range(len(x)):
        a=state[x[i]]
        b=state[y[i]]
        if op=='AND':
            if a and b: s+='-'
            else:       s+='_'
        if op=='OR':
            if a or b:  s+='-'
            else:       s+='_'
        if op=='XOR':
            if a^b:     s+='-'
            else:       s+='_'
        if op=='NAND':
            if a and b: s+='_'
            else:       s+='-'
        if op=='NOR':
            if a or b:  s+='_'
            else:       s+='-'
        if op=='NXOR':
            if a^b:     s+='_'
            else:       s+='-'
    return s

state={'-':1,'_':0}
sig={}
opes=[]

n = int(input())
m = int(input())
for i in range(n):
    input_name, input_signal = input().split()
    sig[input_name]=input_signal
#print(sig, file=sys.stderr, flush=True)

for i in range(m):
    opes.append(input().split())
#print(opes, file=sys.stderr, flush=True)

for i in range(m):
    # sig[opes[i][0]]=logic(opes[i][1],sig[opes[i][2]],sig[opes[i][3]])
    # print(f'{opes[i][0]} {sig[opes[i][0]]}')
    print(f'{opes[i][0]} {logic(opes[i][1],sig[opes[i][2]],sig[opes[i][3]])}')