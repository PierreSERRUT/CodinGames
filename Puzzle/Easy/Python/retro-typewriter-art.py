#retro-typewriter-art
#python

import sys
import math

dict={'sp':' ','bS':'\\','sQ':'\''}

t = input().split(' ')
print(t,file=sys.stderr, flush=True)

s=''
for i in t: 
    if i=='nl': 
        print(s)
        s=''
    else:
        ind=0
        for j in i:
            if j>='0' and j<='9':
                ind+=1
        if ind==len(i): ind-=1
        if i[ind:] not in dict: s+=i[ind:]*int(i[:ind])
        else: s+=dict[i[ind:]]*int(i[:ind])
print(s)