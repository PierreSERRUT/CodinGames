#reverse-minesweeper
#python

import sys
import math

lines=[]
w = int(input())
h = int(input())
for i in range(h):
    lines.append(input())

mat=[]
for i in range(h):
    mat.append([])
    for j in range(w):
        mat[i].append(0)

for i in range(h):
    for j in range(w):
        if lines[i][j]=='x':
            mat[i][j]='.'
            if i>0: 
                if mat[i-1][j]!='.':        mat[i-1][j]+=1
                if j>0:
                    if mat[i-1][j-1]!='.':  mat[i-1][j-1]+=1
                if j<w-1:
                    if mat[i-1][j+1]!='.':  mat[i-1][j+1]+=1
            if i<h-1:
                if mat[i+1][j]!='.':        mat[i+1][j]+=1
                if j<w-1:
                    if mat[i+1][j+1]!='.':  mat[i+1][j+1]+=1
                if j>0:
                    if mat[i+1][j-1]!='.':  mat[i+1][j-1]+=1
            if j<w-1:
                if mat[i][j+1]!='.':        mat[i][j+1]+=1
            if j>0:
                if mat[i][j-1]!='.':        mat[i][j-1]+=1

for i in range(h):
    s=''
    for j in range(w):
        if mat[i][j]==0:
            mat[i][j]='.'
        s+=str(mat[i][j])
    print(s)