m=input()
b=n=o=""
for c in m:
    n+=f'{ord(c):07b}'
for c in n:
    if c=="1"!=b:
        o+=" 0 "
        b="1"
    elif c=="0"!=b:
        o+=" 00 "
        b="0"
    o+="0"
print(o[1:])