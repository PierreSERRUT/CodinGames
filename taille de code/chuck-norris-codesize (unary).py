p=-1
n=0
s=r=''
for i in input():r+=format(ord(i),'08b')[1:]
for i in r:
    if p==i:n+=1
    elif p!=-1:s+='0'*n+' '
    if p!=i:
        v=i
        if v=='1':s+='0 '
        else:s+='00 '
        n=1
    p=i
print(s+'0'*n)