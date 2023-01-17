import sys
import math
import random

def autour(x,y,gx,gy):
    if (gx == x or gx == x-1 or gx == x+1) and (gy == y or gy == y-1 or gy == y+1):
        return True
    return False
    
def bar(points,nb):
    sumx=0
    sumy=0
    for i in points: sumx+=i[0]
    for i in points: sumy+=i[1]
    return sumx//nb , sumy//nb  

def update_pos(dir, x, y):
#     print(file=sys.stderr,flush=True)
#     print('fonction update_pos !',file=sys.stderr,flush=True)
#     print(f'dir:{dir}',file=sys.stderr,flush=True)
#     print(f'x:{x};y:{y}',file=sys.stderr,flush=True)

    if 'N' in dir:
        y-=1
    elif "S" in dir:
        y+=1
    if "E" in dir:
        x+=1
    elif "W" in dir:
        x-=1
    #print(f'x:{x};y:{y}',file=sys.stderr,flush=True)
    return x,y

def direction(x1,y1,x2,y2):
    #print(file=sys.stderr,flush=True)
    dest=''
    destX=''
    destY=''
    
    delta_x=x2 - x1
    delta_y=y2 - y1

    if delta_y > 0: 
        destY+="S"
    elif delta_y < 0:
        destY+="N"
        
    if delta_x > 0 : 
        destX+="E"
    elif delta_x < 0 :
        destX+="W"
    dest = destY + destX
    x1,y1=update_pos(dest,x1,y1)
    if dest=='': dest='WAIT'
    return dest, x1, y1

limite_x=40
limite_y=18

tx, ty = [int(i) for i in input().split()]

while True:
    
    # h: the remaining number of hammer strikes.
    giants=[]
    destination=''
    in_range=0
    possible_dir=8
    dest_imp={'N':0,'NE':0,'E':0,'SE':0,'S':0,'SW':0,'W':0,'NW':0}
    h, n = [int(i) for i in input().split()]
    for i in range(n):
        x, y = [int(j) for j in input().split()]
        giants.append([x,y])
    print(giants,file=sys.stderr,flush=True)

    xb,yb=bar(giants,n)
    #print(f'xb:{xb};yb:{yb}',file=sys.stderr,flush=True)
    destination, xs, ys = direction(tx,ty,xb,yb)
    #print(f'dest:{destination};xs:{xs};ys:{ys}',file=sys.stderr,flush=True)

    for i in giants:
        if autour(tx,ty,i[0],i[1]):
            in_range+=1
            d_imp, xi, yi = direction(tx,ty,i[0],i[1])
            #print(f'd_imp:{d_imp}',file=sys.stderr,flush=True)

            if d_imp in dest_imp:
                dest_imp[d_imp]=1
    for i in dest_imp:
        possible_dir-=dest_imp[i]
    
    print(f'possible_dir:{possible_dir}',file=sys.stderr,flush=True)
    print(f'dest_imp:{dest_imp}',file=sys.stderr,flush=True)
    
    dest_imp['rand']=1
    tmp='rand'
    while dest_imp[tmp] != 0:
        tmp=random.choice(list(dest_imp.keys()))
        print(f'tmp:{tmp};dest_imp[tmp]:{dest_imp[tmp]}',file=sys.stderr,flush=True)

    destination=tmp
    print(file=sys.stderr,flush=True)

    xs,ys=update_pos(destination,tx,ty)

    # The movement or action to be carried out: WAIT STRIKE N NE E SE S SW W or N
    if in_range==n or possible_dir==0:   print('STRIKE')
    else:           
        tx=xs
        ty=ys
        print(destination)
