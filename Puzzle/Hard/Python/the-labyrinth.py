#the-labyrinth
#https://www.codingame.com/ide/puzzle/the-labyrinth
#python

import sys
import math

def Debug(var_name,v):
    print(var_name,v, file=sys.stderr, flush=True)

def print_matrice(r,matrix):
    for i in range(r):
        print("row %02d: %02s" % (i,matrix[i]), file=sys.stderr, flush=True)
    return

def print_autour(matrix):
    Debug('element pos rick:',matrix[pos_rick.r][pos_rick.c])
    Debug('G:',matrix[pos_rick.r][pos_rick.c-1])
    Debug('D:',matrix[pos_rick.r][pos_rick.c+1])
    Debug('H:',matrix[pos_rick.r-1][pos_rick.c])
    Debug('B:',matrix[pos_rick.r+1][pos_rick.c])
    return

def print_chemin(matrix,chem):
    print("chemin:", file=sys.stderr, flush=True)
    for i in chem:
        print("%2d;%2d" % (i.r,i.c), file=sys.stderr, flush=True)

def if_not_in_chemin(r,c,chem):
    for i in chem:
        if r==i.r and c==i.c:
            return False
    return True

def index_chem (r,c,chem):
    for i in range(len(chem)):
        if r==chem[i].r and c==chem[i].c:
            return i

def dest(p1,p2):
    d=''
    if p1.r<p2.r:
        d+='U'
    elif p1.r>p2.r:
        d+='D'
    if p1.c<p2.c:
        d+='R'
    elif p1.c>p2.c:
        d+='L'
    return d

class position:
    def __init__(self,r,c):
        self.r=r
        self.c=c

class poste_commande:
    def __init__(self,p,a,dest,pos):
        self.presence=p
        self.atteint=a
        self.dest=dest
        self.pos=pos

class start:
    def __init__(self,pos,dest):
        self.debut=0
        self.presence=0
        self.pos=pos
        self.dest=dest

# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in input().split()]

chemin_aller=[]
com=poste_commande(0,0,'',position(0,0))
pos_start=start(position(0,0),'')
# game loop
while True:
    matrix=[]
    #Rick pos
    kr, kc = [int(i) for i in input().split()]
    pos_rick=position(kr,kc)
    #matrice
    for i in range(r):
        row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        matrix.append(row)
    print_matrice(r,matrix)
    #pos de depart
    if pos_start.debut==0:
        for i in range(r):
            for j in range(c):
                if matrix[i][j]=='T':
                    pos_start.pos=position(i,j)
                    pos_start.presence=1
                    break
                if pos_start.presence==1: break
        pos_start.debut=1
    
    #detect si com en visu
    if com.presence==0:
        for i in range(r):
            for j in range(c):
                if matrix[i][j]=='C':
                    com.pos=position(i,j)
                    com.presence=1
                    break
                if com.presence==1: break
    #dest Com
    if com.presence == 1:
        com.dest=dest(pos_rick,com.pos)
    
    Debug("com.dest: ",com.dest)
    #detect Com atteint
    if matrix[pos_rick.r][pos_rick.c] == 'C':
        com.atteint=1

    #affichage debug
    Debug("Start", ": ")
    Debug(pos_start.pos.r,pos_start.pos.c)
    if com.presence==1:     Debug("Com", ": "); Debug(com.pos.r,com.pos.c)

    #getion direction
    if com.atteint == 0:
        #ALLER

        #UTILISATION de la direction est important (cf funct dest)


        #idée:

        #voir forum : https://www.codingame.com/forum/t/the-labyrinth-puzzle-discussion/59/24

        #1:  Ajout chemin direction

        #2
        #For all 4 directions:
        # if it is possible to move (i.e. if it’s not a wall, and if it’s not the control room) and if it’s not marked
        # move in that direction
        # explore from the new position (recursive call).
        # move in the opposite direction (i.e. go back).


        chemin_aller.append(pos_rick)
        print_chemin(matrix,chemin_aller)
        d_possible=''
        #print_autour(matrix)
        if pos_rick.r>0:
            #check a gauche
            tmp=matrix[pos_rick.r][pos_rick.c-1]
            if tmp=="." or tmp=="T" or tmp=="C":
                d_possible+='L'
        if pos_rick.r<r:
            #check a droite
            tmp=matrix[pos_rick.r][pos_rick.c+1]
            if tmp=="." or tmp=="T" or tmp=="C":
                d_possible+='R'
        if pos_rick.c>0:
            #check en haut
            tmp=matrix[pos_rick.r-1][pos_rick.c]
            if tmp=="." or tmp=="T" or tmp=="C":
                d_possible+='U'
        if pos_rick.c<c:
            #check en bas
            tmp=matrix[pos_rick.r+1][pos_rick.c]
            Debug("B:",tmp)

            if tmp=="." or tmp=="T" or tmp=="C":
                d_possible+='D'

        Debug('d_possible:',d_possible)
 
        if 'R' in d_possible and if_not_in_chemin(pos_rick.r,pos_rick.c+1,chemin_aller):
            direction="RIGHT"
        elif 'L' in d_possible and if_not_in_chemin(pos_rick.r,pos_rick.c-1,chemin_aller):
            direction="LEFT"
    
        if 'U' in d_possible and if_not_in_chemin(pos_rick.r-1,pos_rick.c,chemin_aller):
            direction="UP"
        elif 'D' in d_possible and if_not_in_chemin(pos_rick.r+1,pos_rick.c,chemin_aller):
            direction="DOWN"

        print(direction)
    else:
        #RETOUR
        Debug("Alarm:",a)
        #calcul chemin retour à faire ici
        
        print_chemin(matrix,chemin_aller)

        if not if_not_in_chemin(pos_rick.r,pos_rick.c,chemin_aller):
            chemin_aller.pop(index_chem(pos_rick.r,pos_rick.c,chemin_aller))
        if not if_not_in_chemin(pos_rick.r,pos_rick.c+1,chemin_aller):
            direction="RIGHT"
        elif not if_not_in_chemin(pos_rick.r,pos_rick.c-1,chemin_aller):
            direction="LEFT"
    
        if not if_not_in_chemin(pos_rick.r-1,pos_rick.c,chemin_aller):
            direction="UP"
        elif not if_not_in_chemin(pos_rick.r+1,pos_rick.c,chemin_aller):
            direction="DOWN"
            
        print(direction)
