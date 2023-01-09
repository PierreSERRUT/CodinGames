#there-is-no-spoon-episode-1
#python

import sys
import math
class node:
    def __init__(self,x1,y1):
        self.x1=x1
        self.y1=y1
        self.x2=-1
        self.y2=-1
        self.x3=-1
        self.y3=-1
    def conv_str(self):
        self.sx1=str(self.x1)
        self.sy1=str(self.y1)
        self.sx2=str(self.x2)
        self.sy2=str(self.y2)
        self.sx3=str(self.x3)
        self.sy3=str(self.y3)
nodes=[]
lines=[]
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    lines.append(input())  # width characters, each either 0 or .
    for j in range(width):
        if lines[i][j] == '0':
           nodes.append(node(j,i))
   
for i in range(len(nodes)):
    indx=indy=-1
    xmin=width+1
    ymin=height+1
    for j in range(len(nodes)):
        tmp=nodes[j].x1-nodes[i].x1
        if tmp < xmin and tmp > 0 and nodes[j].x1!=nodes[i].x1 and nodes[j].y1==nodes[i].y1:
            xmin=tmp
            indx=j
        tmp=nodes[j].y1-nodes[i].y1
        if tmp <ymin and tmp > 0 and nodes[j].y1!=nodes[i].y1 and nodes[j].x1==nodes[i].x1:
            ymin=tmp
            indy=j

    if indx!=-1:
        nodes[i].x2=nodes[indx].x1
        nodes[i].y2=nodes[indx].y1
    if indy!=-1:
        nodes[i].x3=nodes[indy].x1
        nodes[i].y3=nodes[indy].y1

    nodes[i].conv_str()
    print(nodes[i].sx1+' '+ nodes[i].sy1+' '+nodes[i].sx2+' '+ nodes[i].sy2+' '+ nodes[i].sx3+' '+ nodes[i].sy3)
