#telephone-numbers
#python

import sys
import bisect

n_tel=[]
n = int(input())
print(n,file=sys.stderr, flush=True)
for i in range(n):
    tel = input()
    bisect.insort(n_tel, tel) 
print(n_tel,file=sys.stderr, flush=True)

count=len(n_tel[0])
for i in range(n-1):
    j=i+1
    #print('i:',i,'tel-i:',n_tel[i],'tel-j:',n_tel[j],file=sys.stderr, flush=True)
    inclus=1
    l=min(len(n_tel[i]),len(n_tel[j]))
    #print('l:',l,file=sys.stderr, flush=True)
    for k in range(l):
        #print('n_tel[',i,'][',k,']',n_tel[i][k],file=sys.stderr, flush=True)
        if n_tel[i][k] != n_tel[j][k]:
            count+=len(n_tel[j])-k
            inclus=0
            break
    if len(n_tel[i])<len(n_tel[j]) and inclus == 1:  count+=len(n_tel[j])-l
    #print('count:',count,file=sys.stderr, flush=True)
print(count)