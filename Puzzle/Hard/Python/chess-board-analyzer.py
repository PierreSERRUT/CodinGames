#chess-board-analyzer
#python 3

import sys
import math

def def_cases(b, cases, x, y):
    # print('def_case:',file=sys.stderr, flush=True)
    # print(f'x,y:{x},{y}',file=sys.stderr, flush=True)

    cases.append((x,y))
    if y>0 :
        cases.append((x,y-1))
    if y<7 :
        cases.append((x,y+1))
    if x>0 :
        cases.append((x-1,y))
    if x>0 and y>0 :
        cases.append((x-1,y-1))
    if x>0 and y<7 :
        cases.append((x-1,y+1))
    if x<7 :
        cases.append((x+1,y))
    if x<7 and y>0 :
        cases.append((x+1,y-1))
    if x<7 and y<7 :
        cases.append((x+1,y+1))


#dia montante a vérif
def threat(b, case, a_pieces, b_pieces):
    x=case[0]
    y=case[1]
    check=0
    c=b[x][y]
    print('threat:',file=sys.stderr, flush=True)
    print(f'x,y: {x},{y} = {c}',file=sys.stderr, flush=True)
    if c!='.' and c.isupper():  
        p=Piece(c.lower(), 'w', x, y)
    elif c!='.':               
        p=Piece(c.lower(), 'b', x, y)
    else:
        p=Piece(c.lower(), '.', x, y)

    for i in a_pieces:
        #print(f'i / name,x,y: {i.x},{i.y}',file=sys.stderr, flush=True)
        if case=='.' or i.name!=p.name or i.x!=p.x or i.y!=p.y or i.color!=p.color :
            print('if: i', i.x,i.y,file=sys.stderr, flush=True)
            block=0
            check=0
            if check==0 and (i.name=='r' or i.name=='q') and i.x==x:     #ligne
                print('lig',file=sys.stderr, flush=True)

                check=1
                for j in b_pieces:
                    if j.name!='k' and j.x==x and ((j.y<y and j.y>i.y) or (j.y>y and j.y<i.y)):
                        block=1
                        break
                for j in a_pieces:
                    if j.name!='k' and j.x==x and ((j.y<y and j.y>i.y) or (j.y>y and j.y<i.y)):
                        block=1
                        break
                
            elif check==0 and (i.name=='r' or i.name=='q') and i.y==y:   #col
                print('col',file=sys.stderr, flush=True)
                check=1
                for j in b_pieces:
                    if j.name!='k' and j.y==y and ((j.x<x and j.x>i.x) or (j.x>x and j.x<i.x)):
                        block=1
                        break
                for j in a_pieces:
                    if j.name!='k' and j.y==y and ((j.x<x and j.x>i.x) or (j.x>x and j.x<i.x)):
                        block=1
                        break
            
            elif check==0 and (i.name=='b' or i.name=='q'):
                print('diago',file=sys.stderr, flush=True)
                if x==y and i.x==i.y:    #diago desc centré
                    check=1
                    for j in b_pieces:
                        if j.name!='k' and j.y==j.x and ((j.x<x and j.x>i.x) or (j.x>x and j.x<i.x)):
                            block=1
                            break
                    for j in a_pieces:
                        if j.name!='k' and j.y==j.x and ((j.x<x and j.x>i.x) or (j.x>x and j.x<i.x)):
                            block=1
                            break
                
                elif x>y and i.x-i.y == x-y:  # diago desc 1 
                    check=1
                    for j in b_pieces:
                        if j.name!='k' and j.x-j.y == x-y and ((j.x<x and j.x>i.x) or (j.x>x and j.x<i.x)):
                            block=1
                            break
                    for j in a_pieces:
                        if j.name!='k' and j.x-j.y == x-y and ((j.x<x and j.x>i.x) or (j.x>x and j.x<i.x)):
                            block=1
                            break


                elif x<y and i.y-i.x == y-x:  # diago desc 2
                    check=1
                    for j in b_pieces:
                        if j.name!='k' and j.y-j.x == y-x and ((j.x<x and j.x>i.x) or (j.x>x and j.x<i.x)):
                            block=1
                            break
                    for j in a_pieces:
                        if j.name!='k' and j.y-j.x == y-x and ((j.x<x and j.x>i.x) or (j.x>x and j.x<i.x)):
                            block=1
                            break


                elif y==(-x+i.y+i.x):           # diago mont (a vérifier)
                    check=1
                    for j in b_pieces:
                        if j.name!='k' and y==(-x+j.y+j.x) and ((j.x<x and j.x>i.x) or (j.x>x and j.x<i.x)):
                            block=1
                            break
                    for j in a_pieces:
                        if j.name!='k' and y==(-x+j.y+j.x) and ((j.x<x and j.x>i.x) or (j.x>x and j.x<i.x)):
                            block=1
                            break
            elif check==0 and i.name=='n' and ((y==i.y-2 and (x==i.x-1 or x==i.x+1)) or (y==i.y+2 and (x==i.x-1 or x==i.x+1)) or (y==i.y-1 and (x==i.x-2 or x==i.x+2)) or (y==i.y+1 and (x==i.x-2 or x==i.x+2))):
                print('n',file=sys.stderr, flush=True)
                check=1
            elif check==0 and i.name=='k' and abs(i.x-x) <=1 and abs(i.y-y) <=1:
                print('k',file=sys.stderr, flush=True)
                check=1
            elif check==0 and i.name=='p':
                print(f'p color: {i.color} / x,y: {i.x},{i.y} ',file=sys.stderr, flush=True)
                if i.color=='w' and x+1==i.x and (y== i.y-1 or y== i.y+1): #w
                    #print(f'p color: {i.color} / x,y: {i.x},{i.y} ',file=sys.stderr, flush=True)
                    check=1
                elif i.color=='b' and x-1==i.x and (y== i.y-1 or y== i.y+1): #b
                    #print(f'p color: {i.color} / x,y: {i.x},{i.y} ',file=sys.stderr, flush=True)
                    check=1

            if check==1 and block==0: 
                    return 1
    return 0

class Piece:
    def __init__(self, name, color, x, y):
        self.name=name
        self.color=color
        self.x=x 
        self.y=y

board=[]
w_piece=[]
b_piece=[]
pieces=[]
for i in range(8):
    board.append(input())
    for j in range(8):
        case=board[i][j]
        if case!='.':
            if case.isupper():  
                w_piece.append(Piece(case.lower(),'w',i,j))
                pieces.append(Piece(case.lower(),'w',i,j))
            else:               
                b_piece.append(Piece(case.lower(),'b',i,j))
                pieces.append(Piece(case.lower(),'b',i,j))
            
        if case.lower()=='k':
            if case.isupper():  w_king=Piece(case.lower(),'w',i,j)
            else:               b_king=Piece(case.lower(),'b',i,j)
    print(board[i],file=sys.stderr, flush=True)

print('kings:',file=sys.stderr, flush=True)
print('w:',w_king.x,w_king.y,file=sys.stderr, flush=True)
print('b:',b_king.x,b_king.y,file=sys.stderr, flush=True)

print(file=sys.stderr, flush=True)
print('W_piece:',file=sys.stderr, flush=True)
for i in w_piece:
    print(i.name,i.x,i.y,file=sys.stderr, flush=True)

print(file=sys.stderr, flush=True)
print('B_piece:',file=sys.stderr, flush=True)
for i in b_piece:
    print(i.name,i.x,i.y,file=sys.stderr, flush=True)

#R col /lig 
#B dia
#Q col /lig /dia
#K toutes les cases autours
#P dia de 1 vers le haut / p dia de 1 vers le haut
w_cases=[]
b_cases=[]

def_cases(board,w_cases,w_king.x,w_king.y)
def_cases(board,b_cases,b_king.x,b_king.y)

w_check=[0]*len(w_cases)
b_check=[0]*len(b_cases)

for i in range(len(w_cases)):
    w_check[i]=threat(board, w_cases[i], b_piece, w_piece)

print(file=sys.stderr, flush=True)
print('--------------------------------',file=sys.stderr, flush=True)
print(file=sys.stderr, flush=True)

for i in range(len(b_cases)):
    b_check[i]=threat(board, b_cases[i], w_piece, b_piece)

print(file=sys.stderr, flush=True)
print('w_cases:',w_cases,file=sys.stderr, flush=True)
print('w_check:',w_check,file=sys.stderr, flush=True)
print('b_cases:',b_cases,file=sys.stderr, flush=True)
print('b_check:',b_check,file=sys.stderr, flush=True)

w_win=1
b_win=1

w='N'
if 0 not in b_check :
    w='W'
elif 0 not in w_check :
    w='B'
elif b_check.count(0)>=1 and b_check[0]==1 :
    for ind, v in enumerate(b_check):
        if v==0:
            print('ind:',ind,file=sys.stderr, flush=True)
            x,y=b_cases[ind][0],b_cases[ind][1]
            print(x,y,file=sys.stderr, flush=True)
            print(f'b({x},{y})= {board[x][y]}',file=sys.stderr, flush=True)
            if board[x][y].islower() and board[x][y]!='.':
                b_check[ind]=1
            elif board[x][y]!='.':
                print("overlaping B",file=sys.stderr, flush=True)

    if 0 not in b_check :
        w='W'
elif w_check.count(0)>=1 and w_check[0]==1 :
    for ind, v in enumerate(w_check):
        if v==0:
            print('ind:',ind,file=sys.stderr, flush=True)
            x,y=w_cases[ind][0],w_cases[ind][1]
            print(x,y,file=sys.stderr, flush=True)
            print(f'b({x},{y})= {board[x][y]}',file=sys.stderr, flush=True)
            if board[x][y].isupper() and board[x][y]!='.' :
                w_check[ind]=1
            elif board[x][y]!='.':
                print("overlaping W",file=sys.stderr, flush=True)
    if 0 not in w_check :
        w='B'
    
print(w)
