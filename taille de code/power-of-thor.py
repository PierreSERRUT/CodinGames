x,y,a,b=[int(i) for i in input().split()]
while 1:
    d=''
    if y>b:d+="S";b+=1
    elif y<b:d+="N";b-=1
    if x>a:d+="E";a+=1
    elif x<a:d+="W";a-=1
    print(d)