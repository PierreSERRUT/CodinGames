#mayan-calculation
#python

import sys
import math
import re

def conv_maya_chiffre(base,maya,l) -> int:
    s=0
    nb=int(len(maya)/l)
    maya = [maya[x:x+l] for x in range(0, len(maya),l)]

    for i in range(nb):
        for j in range(20):
            if base[j] == maya[nb-i-1]: 
                s+=j*(20**i)
                break
    return s

def conv_chiffre_maya(base,ch):
    maya=[]
    tmp=[]
    nb=1
    if ch < 20:
        maya=base[ch]
    else:
        digits = []
        while ch:
            digits.append(int(ch % 20))
            ch //= 20
        b20=digits[::-1]
        for i in b20:
            tmp.append(base[int(i)])
    for i in tmp:
        for j in i:
            maya.append(j)
    return maya

num_1line=[]
num_2line=[]
nums=[]
numero=[]
l, h = [int(i) for i in input().split()]
for i in range(h):
    n=input()
    n_cut = [n[x:x+l] for x in range(0, len(n),l)]

    nums.append(n_cut)

for j in range(len(nums[0])):
    numero.append([])
    for i in range(len(nums)):
        numero[j].append(nums[i][j])

s1 = int(input())
for i in range(s1):
    num_1line.append(input())

s2 = int(input())
for i in range(s2):
    num_2line.append(input())

num1=conv_maya_chiffre(numero,num_1line,l)
num2=conv_maya_chiffre(numero,num_2line,l)

op = input()
if op =='+':
    res=num1+num2
elif op =='-':
    res=num1-num2
elif op =='*':
    res=num1*num2
elif op =='/':
    res=int(num1/num2)

sortie=conv_chiffre_maya(numero,res)
for i in sortie:
    print(i)