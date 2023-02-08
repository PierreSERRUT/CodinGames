#dungeons-and-maps
#python

import sys
import math

w, h = [int(i) for i in input().split()]
#print('w, h:',w, h, file=sys.stderr, flush=True)
s_row, s_col = [int(i) for i in input().split()]
#print('s_row, s_col:',s_row, s_col, file=sys.stderr, flush=True)

n = int(input())
maps=[]
for i in range(n):
    maps.append([])
    for j in range(h):
        map_row = input()
        maps[i].append(map_row)

min_path_len=h*w
ind_path=-1
for i in range(n):
    # print(file=sys.stderr, flush=True)
    # for j in range(h):
    #     print(maps[i][j], file=sys.stderr, flush=True)
    path_len=1
    r=s_row
    c=s_col
    pos=maps[i][r][c]    
    while pos!='T' and pos!='.' and pos!='#':
        if pos=='>':
            c+=1
        elif pos=='<':
            c-=1
        elif pos=='v':
            r+=1
        elif pos=='^':
            r-=1
        path_len+=1

        if r<0 or r>=h or c<0 or c>=w or (r==s_row and c==s_col): break
        pos=maps[i][r][c]

    if pos=='T' and path_len < min_path_len:
        min_path_len = path_len
        ind_path=i
        
if ind_path==-1:    print('TRAP')
else:               print(ind_path)