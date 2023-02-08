#merlins-magic-square
#python
import sys
import math

def action(a,m):
    a=int(a)
    if a==1:
        m[0]=(m[0]+1)%2
        m[1]=(m[1]+1)%2
        m[3]=(m[3]+1)%2
        m[4]=(m[4]+1)%2
    elif a==3:
        m[1]=(m[1]+1)%2
        m[2]=(m[2]+1)%2
        m[4]=(m[4]+1)%2
        m[5]=(m[5]+1)%2
    elif a==7:
        m[3]=(m[3]+1)%2
        m[4]=(m[4]+1)%2
        m[6]=(m[6]+1)%2
        m[7]=(m[7]+1)%2
    elif a==9:
        m[4]=(m[4]+1)%2
        m[5]=(m[5]+1)%2
        m[7]=(m[7]+1)%2
        m[8]=(m[8]+1)%2
    elif a==2: 
        m[0]=(m[0]+1)%2
        m[1]=(m[1]+1)%2
        m[2]=(m[2]+1)%2
    elif a==4:
        m[0]=(m[0]+1)%2
        m[3]=(m[3]+1)%2
        m[6]=(m[6]+1)%2
    elif a==6:
        m[2]=(m[2]+1)%2
        m[5]=(m[5]+1)%2
        m[8]=(m[8]+1)%2
    elif a==8:
        m[6]=(m[6]+1)%2
        m[7]=(m[7]+1)%2
        m[8]=(m[8]+1)%2
    elif a==5:
        m[1]=(m[1]+1)%2
        m[3]=(m[3]+1)%2
        m[4]=(m[4]+1)%2
        m[5]=(m[5]+1)%2
        m[7]=(m[7]+1)%2

state={'~':0,'*':1}
mat=[]
sol=[1,1,1,1,0,1,1,1,1]

for j in range(3):
    [mat.append(state[i]) for i in input().split(' ')]
all_buttons_pressed = input()
# print('mat:',mat,file=sys.stderr, flush=True)
# print('sol:',sol,file=sys.stderr, flush=True)
# print(all_buttons_pressed,file=sys.stderr, flush=True)

for i in all_buttons_pressed:
    action(i,mat)

for i in range(9):
    action(i+1,mat)
    if mat==sol:
        print(i+1)
        break
    else: action(i+1,mat)