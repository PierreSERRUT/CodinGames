#code-vs-zombies
#https://www.codingame.com/ide/puzzle/code-vs-zombies
#python
import sys
from math import sqrt

# Save humans, destroy zombies!
class Human:
    def __init__(self, id, x, y):
        self.id=id
        self.x=x
        self.y=y
    
    def __update__(self, id, x, y):
        self.id=id
        self.x=x
        self.y=y

class Zombie:
    def __init__(self, id, x, y, x_next, y_next):
        self.id=id
        self.x=x
        self.y=y
        self.x_next=x_next
        self.y_next=y_next
        self.hid=None

    def __update__(self, id, x, y, x_next, y_next,hid):
        self.id=id
        self.x=x
        self.y=y
        self.x_next=x_next
        self.y_next=y_next
        self.hid=hid

def Debug(var_name, var):
    print(var_name, var, file=sys.stderr, flush=True)

def Sqr(a):
    return a*a

def Distance(x1,y1,x2,y2):
    return sqrt(Sqr(y2-y1)+Sqr(x2-x1))

# game loop
while True:
    humans=[]
    #humans={}
    zombies=[]

    x, y = [int(i) for i in input().split()]
    ash=Human(-1,x,y)
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans.append(Human(human_id, human_x, human_y))
        #humans[human_id]={'x':human_x, 'y':human_y}
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombies.append((Zombie(zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext)))

    # for hid, human in humans.items():
    #         for zid, zomb in zombies:
    #             if (zomb['xn'] > human['x'] - 600 or zomb['xn'] < human['x'] + 600) and (
    #                     zomb['yn'] > human['y'] - 600 or zomb['yn'] < human['y'] + 600):
    #                 zombie_attack_human[zid] = hid

    dist_mini = Distance(0,0,16000,9000)
    dist_ash = Distance(ash.x,ash.y,humans[0].x,humans[0].y)
    Debug('first dist:',dist_mini)
    
    h_danger=Human(-2,humans[0].x,humans[0].y)
    
    for i in range(human_count):
        dist_ash = Distance(ash.x,ash.y,humans[i].x,humans[i].y)
        nb_t_ash = (dist_ash - 2000 )/1000
        Debug('Human:',i)
        Debug('nb_t_ash:',nb_t_ash)
        for j in range(zombie_count):
            dist = Distance(humans[i].x,humans[i].y,zombies[j].x,zombies[j].y)
            nb_t_z = dist/400
            Debug('nb_t_z:',nb_t_z)
            #Debug('dist:',dist)     
            #Debug('dist_mini:',dist_mini)
            if dist < dist_mini and nb_t_ash < nb_t_z:
                dist_mini = dist
                h_danger.__update__(-2,humans[i].x,humans[i].y)
    
    dest=str(h_danger.x )+' '+str(h_danger.y)

    # Your destination coordinates
    print(dest)