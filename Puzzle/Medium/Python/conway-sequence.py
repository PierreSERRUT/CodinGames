#conway-sequence
#python

import sys
import math

r=int(input())
l = int(input())
s=[]
s.append(r)
for i in range(l-1):
    c=0
    tmp=[]
    for j in range(len(s)):
        if j==0:
            val=s[j]
            c+=1
        else:
            if s[j] == val: c+=1
            else:
                tmp.append(c)
                tmp.append(val)
                c=1
                val=s[j]
    tmp.append(c)
    tmp.append(val)
    s=tmp
print(*s)