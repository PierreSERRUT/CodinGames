#cgx-formatter
#python

import sys
import math

cgx=''
n = int(input())
for i in range(n):
    cgx+=(input())+'~'

s=''
p_p=0
e_p=0
l=len(cgx)
index_g=0
p_g=0
pv=0

for j in range(l):
    c_ascii=ord(cgx[j])

    if cgx[j]!=' ' and cgx[j]!='~': # espace
        
        if c_ascii!=9 and c_ascii!=40 and c_ascii!=41: #/tab
            if cgx[j]=='\'': # ' text  '
                if p_g==0:
                    index_g=j
                    p_g=1
                else:
                    s+=cgx[index_g:j+1]
                    p_g=0
            elif p_g==0:
                s+=cgx[j]
        
        if c_ascii==40 and p_g!=1: #(
            if s!='':
                print(('    '*p_p)+s)
                s=''
            print(('    '*p_p)+'(')
            p_p+=1
        
        if c_ascii==41 and p_g!=1: #)
            e_p=0
            if s!='':
                print(('    '*p_p)+s)
                s=''
            if j<l-1 and cgx[j+1]==';':
                print(('    '*(p_p-1))+');')
                pv=1
            else: print(('    '*(p_p-1))+')')
            p_p-=1
        
        if c_ascii==59 and p_g!=1: # ;
            e_p=0
            if pv==0:
                if s!='':
                    print(('    '*p_p)+s)
                    s=''
            else: 
                s=s[:-1]
                pv=0
        
        if c_ascii==61: #=
            e_p=1
    if e_p==0 and cgx[j]=='~' and s!='':
        print(('    '*p_p)+s)
        s=''  
print(s)