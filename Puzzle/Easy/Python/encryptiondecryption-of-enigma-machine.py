#encryptiondecryption-of-enigma-machine
#python

import sys
import math

def caesar_shift(n: int, m: str) -> str:
    s=''
    for i in range(len(m)):
        tmp=ord(m[i])+n+i
        while tmp>90:   tmp-=26
        s+=chr(tmp)
    return s

def rev_caesar_shift(n: int, m: str) -> str:
    s=''
    for i in range(len(m)):
        tmp=ord(m[i])-n-i
        while tmp<65:   tmp+=26
        s+=chr(tmp)
    return s

def inv_rot(dic, val):
    return list(filter(lambda x: dic[x] == val, dic))[0]

rotor1={'A':'','B':'','C':'','D':'','E':'','F':'','G':'','H':'','I':'','J':'','K':'','L':'','M':'','N':'','O':'','P':'','Q':'','R':'','S':'','T':'','U':'','V':'','W':'','X':'','Y':'','Z':'',}
rotor2={'A':'','B':'','C':'','D':'','E':'','F':'','G':'','H':'','I':'','J':'','K':'','L':'','M':'','N':'','O':'','P':'','Q':'','R':'','S':'','T':'','U':'','V':'','W':'','X':'','Y':'','Z':'',}
rotor3={'A':'','B':'','C':'','D':'','E':'','F':'','G':'','H':'','I':'','J':'','K':'','L':'','M':'','N':'','O':'','P':'','Q':'','R':'','S':'','T':'','U':'','V':'','W':'','X':'','Y':'','Z':'',}
op = input()
pseudo_random_number = int(input())
rotors=[]
for i in range(3):
    rotors.append(input())

c=0
for i in rotor1:
    rotor1[i]=rotors[0][c]
    rotor2[i]=rotors[1][c]
    rotor3[i]=rotors[2][c]
    c+=1

mess = input()
s=''
if op == 'ENCODE':
    mess=caesar_shift(pseudo_random_number,mess)
    for i in mess:
        s+=rotor3[rotor2[rotor1[i]]]
else:
    for j in mess:
        k1 = inv_rot(rotor3,j)
        k2 = inv_rot(rotor2,k1)
        s += inv_rot(rotor1,k2)
    s=rev_caesar_shift(pseudo_random_number,s)

print(s)