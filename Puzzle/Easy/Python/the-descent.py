#the-descent
#python

import sys
import math

while True:
    mountains = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        mountains.append(mountain_h)

    index=0
    max_hight=0
    for j in range(8):
        if mountains[j] > max_hight:
            index=j
            max_hight=mountains[j]
            #print('index:',index,',max_hight:',max_hight, file=sys.stderr, flush=True)
    print(index)
