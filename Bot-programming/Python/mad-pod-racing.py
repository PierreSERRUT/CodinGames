#mad-pod-racing
#https://www.codingame.com/multiplayer/bot-programming/mad-pod-racing
#python

import sys
import math

def debug(var_name, var):
    print(var_name, var, file=sys.stderr, flush=True)

class list_point:
    def __init__(self):
        self.x = []
        self.y = []
    
    def __getitemX__(self, nb):
        return self.x[nb]

    def __getitemY__(self, nb):
        return self.y[nb]

    def __add__(self, var ):   
        self.x.append(var.x)
        self.y.append(var.y)

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitemX__(self):
        return self.x

    def __getitemY__(self):
        return self.y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return point(x, y)

    def __mul__(self, num):
        x = self.x * num
        y = self.y * num
        return point(x, y)

#init var
boost_used=0
first_run=0

#var cp et tour
nb_cp=0    #cp_x.__len__
nb_cp_tot=0
tour=0
cp = []
#cp_x=[]
#cp_y=[]

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    if first_run == 0:
        first_run = 1  
        #dest_x =next_checkpoint_x
        #dest_y =next_checkpoint_y  
        dest=point(next_checkpoint_x,next_checkpoint_y)
    else:
        #past_dest_x=dest_x
        #past_dest_y=dest_y
        #dest_x =next_checkpoint_x
        #dest_y =next_checkpoint_y
        past_dest=point(dest.x,dest.y)
        dest=point(next_checkpoint_x,next_checkpoint_y)
        #debug("past_dest_x", past_dest.x)
        #debug("dest_x",dest.x)

        #if past_dest_x != dest_x and past_dest_y != dest_y:
        if past_dest.x != dest.x and past_dest.y != dest.y:
            #cp_x.append(past_dest_x)
            #cp_y.append(past_dest_y)
            if nb_cp ==0:
                cp.append(past_dest)
                nb_cp+=1
            #vérif si tour, à mod
            else:
                tmp=0
                for i in range(nb_cp -1 ):
                    debug("for i:",i)
                    debug("past_dest_x", past_dest.x)
                    debug("x:",cp[i].x)
                    if past_dest.x == cp[i].x and past_dest.y == cp[i].y :
                        tmp=1
                        break
                    else:
                        tmp=0
                    debug("for",nb_cp-1)
                    debug("i:",i)
                    debug("tmp:",tmp)
                if tmp==0:
                    cp.append(past_dest)
                    nb_cp+=1     
                else:
                    tour+=1
                    nb_cp_tot=nb_cp
            # for i in range(nb_cp -1 ):
            #     debug("affichage i:",i)
            #     debug("x:",cp[i].x)
            #     debug("y:",cp[i].y)      
    debug("nb_cp",nb_cp)
    debug("tour",tour)
    debug("nb_cp_tot",nb_cp_tot)
    debug('lentgh',cp.__len__())
    #print("initial_x",initial_x, file=sys.stderr, flush=True)
   
    if abs(next_checkpoint_angle) > 144 :
        thurst = 25
    elif abs(next_checkpoint_angle) > 108 :
        thurst = 45
    elif abs(next_checkpoint_angle) > 72 :
        thurst = 65 
    elif abs(next_checkpoint_angle) > 36 :
        thurst = 90
    else:
        thurst = 100
    
    # PASSAGE ARGENT
    # if next_checkpoint_angle > 135 or next_checkpoint_angle < -135 :
    #     thurst = 25 
    # elif next_checkpoint_angle > 90 or next_checkpoint_angle < -90 :
    #     thurst = 50
    # else:
    #     thurst = 100
    
    #Virage
    #lineaire
    #thurst=100 - (int(0.444*abs(next_checkpoint_angle)))
    # #lineaire 2
    # if abs(next_checkpoint_angle) > 20:
    #     thurst=110 - (int(0.50*abs(next_checkpoint_angle)))
    # else:
    #     thurst=100
    #lineaire 3
    # if abs(next_checkpoint_angle) > 30 and next_checkpoint_dist < 2000:
    #     thurst=int((116 - (int(0.5333*abs(next_checkpoint_angle)))) *(0.7 - 0.00015*next_checkpoint_dist))
    # elif abs(next_checkpoint_angle) > 30:
    #     thurst=116 - (int(0.5333*abs(next_checkpoint_angle)))
    # elif next_checkpoint_dist < 2000:
    #     thurst=int(70 - 0.015*next_checkpoint_dist)
    # else:
    #     thurst=100

    #test4
    # if abs(next_checkpoint_angle) > 30 and next_checkpoint_dist < 2000:
    #     thurst=int((116 - (int(0.5333*abs(next_checkpoint_angle)))) *(0.8 - 0.0000066667*next_checkpoint_dist))
    # elif abs(next_checkpoint_angle) > 30:
    #     thurst=116 - (int(0.5333*abs(next_checkpoint_angle)))
    # elif next_checkpoint_dist < 2000:
    #     thurst=int(80 - 0.0066667*next_checkpoint_dist)
    # else:
    #     thurst=100
    
    #test5
    # if next_checkpoint_dist< 5000:
    #     thurst=int(20.5046 + 0.0274083*next_checkpoint_dist)
    # else:
    #     thurst=thurst=int(114 - 0.46667*abs(next_checkpoint_angle))
    # if thurst > 100:
    #     thurst=100
    
    # print('vit',thurst,'angle',next_checkpoint_angle,'dist',next_checkpoint_dist,file=sys.stderr, flush=True) 

    if next_checkpoint_dist < 800:
        dest.__add__(point(100,100))

    # i.e.: "x y thrust"
   
    if next_checkpoint_dist > 7000 and abs(next_checkpoint_angle) < 10 and boost_used != 1 : 
        print(str(dest.x) + " " + str(dest.y) + " BOOST")
        boost_used=1
    else:
        print(str(dest.x) + " " + str(dest.y) + " " + str(thurst))
