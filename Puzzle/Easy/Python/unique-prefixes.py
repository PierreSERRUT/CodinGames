#unique-prefixes
#python

import sys
import math

words=[]
n = int(input())
for i in range(n):
    words.append(input())
for i in words:
    smax=''
    for j in words:
        s=''
        index=-1
        if i!=j:
            for k,v in enumerate(i):
                if k < len(j) and v==j[k]:
                    s+=v
                    index=k
                else: break

        if len(i)>index+1:
            s+=i[index+1]
        if len(s)> len(smax): smax=s
    print(smax)