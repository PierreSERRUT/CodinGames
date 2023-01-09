#death-first-search-episode-1
#python

import sys
import math
from collections import deque

def Debug(var_name):
    print(var_name, file=sys.stderr, flush=True)

def BFS_SP(graph, start, goal):
	explored = []
	queue = [[start]]
	while queue:
		path = queue.pop(0)
		node = path[-1]
		
		if node not in explored:
			neighbours = graph[node]
			
			for neighbour in neighbours:
				new_path = list(path)
				new_path.append(neighbour)
				queue.append(new_path)
				
				if neighbour == goal:
					return new_path
			explored.append(node)

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

def find_paths_dfs(graph, start, end):
    stack = deque()
    stack.append((start, [start]))

    while stack:
        (node, path) = stack.pop()
        adjacent_nodes = [n for n in graph[node] if n not in path]
        for adjacent_node in adjacent_nodes:
            if adjacent_node == end:
                yield path + [adjacent_node]
            else:
                stack.append((adjacent_node, path + [adjacent_node]))
    
class link:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
links=[]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]

    links.append(link(n1,n2))
    links.append(link(n2,n1))

gates=[]
for i in range(e):
    gates.append(int(input()))  # the index of a gateway node

graph={}
for i in range(n):
    tmp=[]
    for j in range(l*2):
        if links[j].n1==i:
            tmp.append(links[j].n2)
    graph[i]=sorted(tmp)

while True:
    n_min=-1
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    for i in gates:
        # p=find_path(graph,si,i)

        p2=BFS_SP(graph,si,i)
        print('p2:',p2, file=sys.stderr, flush=True)
        if p2!=None:
            if len(p2)<n_min or n_min<0:
                    p_min=p2
                    n_min=len(p2)

        # for j in find_paths_dfs(graph,si,i):
        #     if len(j)<n_min or n_min<0:
        #         p_min=j
        #         n_min=len(j)

    graph[(p_min[0])].remove(p_min[1])
    graph[(p_min[1])].remove(p_min[0])
    print(str(p_min[0])+' '+str(p_min[1]))