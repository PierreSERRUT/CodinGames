#unary
#python

import sys
import math

sortie=res=''
val_prec=-1
s_nb=0

for i in input():
    tmp=format(ord(i), '08b')
    res = res + tmp[1:]

for i in res:        
    if val_prec == i: s_nb+=1
    elif val_prec!=-1: 
        sortie=sortie+'0'*s_nb+' '
    if val_prec != i:   
        val_prec=i
        s_val=i
        #print('s:',sortie, file=sys.stderr, flush=True)
        #print('s_val:',s_val, file=sys.stderr, flush=True)
        if s_val=='1':  sortie=sortie+'0 '
        else:           sortie=sortie+'00 '
        s_nb=1
        #print('s:',sortie, file=sys.stderr, flush=True)
    val_prec = i
sortie=sortie+'0'*s_nb
print(sortie)