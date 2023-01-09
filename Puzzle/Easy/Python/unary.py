#unary
#python

import sys
import math

sortie=''
s_val=-1
val_prec=-1
first_one=0
s_nb=0
res=''
for i in input():
    tmp=format(ord(i), '08b')
    #print(tmp, file=sys.stderr, flush=True)
    if len(tmp) > 7: tmp=tmp[1:]
    #print(tmp, file=sys.stderr, flush=True)

    res = res + tmp
#print(res, file=sys.stderr, flush=True)

for i in res:
    #print('i:',i,'s:',sortie, file=sys.stderr, flush=True)

    if val_prec == -1:
        val_prec=i
        s_val=i
        #print('s_val:',s_val, file=sys.stderr, flush=True)
        if s_val=='1':  sortie=sortie.join('0 ')
        else:           sortie=sortie+'0'*2+' '
        s_nb+=1
    elif val_prec == i: s_nb+=1
    else: 
        sortie=sortie+'0'*s_nb+' '
        val_prec=i
        s_val=i
        #print('s:',sortie, file=sys.stderr, flush=True)
        #print('s_val:',s_val, file=sys.stderr, flush=True)
        if s_val=='1':  sortie=sortie+'0 '
        else:           sortie=sortie+'0'*2+' '
        s_nb=1
        #print('s:',sortie, file=sys.stderr, flush=True)

sortie=sortie+'0'*s_nb
print(sortie)