#temperatures
#python

import sys
import math

temp=[]
n = int(input())  # the number of temperatures to analyse
debug("n:",n)
tmp=0
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    temp.append(t)
    
t_proche=5527
if n != 0:
    for i in range(n):
        if abs(temp[i]) < abs(t_proche):
            t_proche = temp[i]
        elif abs(temp[i]) == abs(t_proche):
            if temp[i]>0:
                t_proche=temp[i]
    print(t_proche)
else:
    print('0')
