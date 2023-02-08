#frame-the-picture
#python

import sys
import math


pic=[]
frame=[]
frame_pattern = input()
h, w = [int(i) for i in input().split()]
for i in range(h): pic.append(input())

# print(frame_pattern ,file=sys.stderr, flush=True)
# print(pic ,file=sys.stderr, flush=True)

w_tot=w+(len(frame_pattern)+1)*2
h_tot=h+(len(frame_pattern)+1)*2
#print(f'w: {w} / w_tot: {w_tot}' ,file=sys.stderr, flush=True)
#print(f'h: {h} / h_tot: {h_tot}' ,file=sys.stderr, flush=True)

for i in range(h_tot):
    frame.append([])
    for j in range(w_tot):
        frame[i].append(' ')

for i in range(h_tot):    
    s=''
    for j in range(w_tot):
        a=0
        for ind , val in enumerate(frame_pattern):
            if (i == ind or i == h_tot-1-ind or j == ind or j == w_tot-1-ind) and  frame[i][j] == ' ' :
                s+=val
                frame[i][j]=val
                a=1
        if a==0:
            s+=' '
    for ind, p in enumerate(pic):
        if i == len(frame_pattern)+1+ind:
            s=s[:len(frame_pattern)+1]+p+s[len(frame_pattern)+1+w:]
    print(s)