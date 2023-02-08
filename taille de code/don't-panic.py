k,w,r,ef,ep,z,w,e=[int(i) for i in input().split()]
a={}
for i in range(e):
    af,ap=[int(j) for j in input().split()]
    a[af]=ap
while True:
    f,p,d=input().split()
    f=int(f)
    p=int(p)
    if f==ef:t=ep
    elif f in a:t=a[f]
    r="WAIT"
    if (d=='RIGHT'and p>t)or(d=='LEFT'and p<t):r='BLOCK'
    print(r)