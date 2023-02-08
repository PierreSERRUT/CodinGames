#code-of-the-rings
#python

import sys
import math

magic_phrase = input()
print(magic_phrase, file=sys.stderr, flush=True)

rune=ord('A')-65
print(rune, file=sys.stderr, flush=True)
s=''
ind=0
mem=[]*30
print('mem:',mem, file=sys.stderr, flush=True)

for i in magic_phrase:
    print('i:',i, file=sys.stderr, flush=True)
    if i==' ':  val_l=0
    else:       val_l=ord(i)-64
    dif=abs(rune-val_l)
    print('rune,val_l,dif:',rune,val_l,dif, file=sys.stderr, flush=True)
    if abs(dif)>13:
        val_l-=27
        dif=abs(rune-val_l)

    if val_l>rune:  s+='+'*dif
    else:           s+='-'*dif
    rune=val_l
    s+='.'

print(s)