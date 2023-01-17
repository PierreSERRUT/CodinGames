#1d-spreadsheet
#python3

import sys

def calc(a,b,op):
    if op == 'VALUE':
        return a
    b=int(b)
    if op == 'ADD':
        return a+b
    elif op == 'SUB': 
        return a-b
    elif op == 'MULT': 
        return a*b

n = int(input())

ops=[]
arg_1s=[]
arg_2s=[]
res=['']*n
count=0
ft=1

for i in range(n):
    operation, arg_1, arg_2 = input().split()
    ops.append(operation)
    arg_1s.append(arg_1)
    arg_2s.append(arg_2)
    #res.append('')

while count<n or ft==1:
    if ft==1: ft=0
    for i in range(n):
        a=arg_1s[i]
        b=arg_2s[i]
        if res[i]=='' and ((a[0]!='$' and b[0]!='$') or (a[0]=='$' and res[int(a[1:])]!='' and b[0]!='$') or (b[0]=='$' and res[int(b[1:])]!='' and a[0]!='$') or (a[0]=='$' and b[0]=='$' and res[int(a[1:])]!='' and res[int(b[1:])]!='')):
            if a[0]!='$':   a=int(a)
            else:           a=res[int(a[1:])]
            if b[0]=='$':   b=res[int(b[1:])]
            res[i]=calc(a,b,ops[i])
            count+=1

for i in range (n):
    print(res[i])