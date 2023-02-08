s=5527
if(int(input())==0):print('0')
else:
    for i in input().split(): 
        a=int(i)
        if abs(a)<abs(s) or a==abs(s):s=a
    print(s)