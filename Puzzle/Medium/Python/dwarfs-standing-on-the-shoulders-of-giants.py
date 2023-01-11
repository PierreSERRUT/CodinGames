#dwarfs-standing-on-the-shoulders-of-giants
#python

import sys
import math
import bisect
from collections import deque

def BFS(graph,nodes, u):
    #print(file=sys.stderr, flush=True)
    #print('node u=',u,file=sys.stderr, flush=True)
    distance={}
    for i in nodes: distance[i] = -1
    distance[u] = 0

    queue = deque()
    queue.append(u)

    while queue:
        front = queue.popleft()
        for i in graph[front]:
            distance[i] = distance[front]+1
            queue.append(i)
    #print('dist F:',distance,file=sys.stderr, flush=True)

    maxDis = 0
    for i in nodes:
        if distance[i] > maxDis:
            maxDis = distance[i]
    return maxDis
 
graph={}
nodes=[]
links=[]

n = int(input())  # the number of relationships of influence
for i in range(n):
    x, y = [int(j) for j in input().split()]
    #print('x:',x,'y:',y, file=sys.stderr, flush=True)
    links.append([x,y])
    if x not in nodes:  bisect.insort(nodes,x)
    if y not in nodes:  bisect.insort(nodes,y)

for i in nodes:
    if i not in graph:  graph[i]=[]
    for j in range(n):
        if links[j][0]==i:
            bisect.insort(graph[i],links[j][1])

# for i in graph:
#     print(f'{i:2.0f} : {graph[i]} ',file=sys.stderr, flush=True)
#print('nodes:',nodes, file=sys.stderr, flush=True)

n_max=-1
for i in nodes:
    n1=BFS(graph,nodes,i)  
    if n1+1>n_max:  n_max=n1+1
print(n_max)