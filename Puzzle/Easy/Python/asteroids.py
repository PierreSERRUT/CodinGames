import sys
import math

ast_t1={}
ast_t2={}

w, h, t1, t2, t3 = [int(i) for i in input().split()]
for i in range(h):
    first_picture_row, second_picture_row = input().split()
    for j in range(w):
        a=first_picture_row[j]
        b=second_picture_row[j]
        if a!='.':
            ast_t1[a]=(i,j)
        if b!='.':
            ast_t2[b]=(i,j)

res = [['.']*w for _ in range(h)]
dt = (t3-t2)/(t2-t1)

for i in sorted(ast_t1, reverse=True):
    if i in ast_t2: 
        delta = ( ast_t2[i][0]-ast_t1[i][0] , ast_t2[i][1]-ast_t1[i][1] )
        x = math.floor(ast_t2[i][0]+delta[0]*dt)
        y = math.floor(ast_t2[i][1]+delta[1]*dt)
        if 0 <= x < h and 0 <= y < w:
            res[x][y] = i

for r in res:
    print(''.join(r))