#scrabble
#python


import sys
import math

def test_point(l,p,dic,a,b,c,d,e,f,g,):
    m=''
    if b==-1:   t=''.join((l[a]))
    elif c==-1: t=''.join((l[a],l[b]))
    elif d==-1: t=''.join((l[a],l[b],l[c]))
    elif e==-1: t=''.join((l[a],l[b],l[c],l[d]))
    elif f==-1: t=''.join((l[a],l[b],l[c],l[d],l[e]))
    elif g==-1: t=''.join((l[a],l[b],l[c],l[d],l[e],l[f]))
    else:       t=''.join((l[a],l[b],l[c],l[d],l[e],l[f],l[g]))
    
    if t in dic:        
        if p <= dic[t]: 
            p=dic[t]
            m=t
    return p,m

dic={}
points={'e':1, 'a':1, 'i':1, 'o':1, 'n':1, 'r':1, 't':1, 'l':1, 's':1, 'u':1, 'd':2, 'g':2, 'b':3, 'c':3, 'm':3, 'p':3, 'f':4, 'h':4, 'v':4, 'w':4, 'y':4, 'k':5, 'j':8, 'x':8, 'q':10, 'z':10}
n = int(input())
for i in range(n):
    w = input()
    w_p=0
    for j in w:
        w_p+=points[j]
    dic[w]=w_p
letters = input()
print(letters, file=sys.stderr, flush=True)
print(dic, file=sys.stderr, flush=True)

tent=''
p_anc=0
p_max=0
mot=''
s=''

for a in range(7):
    p_anc=p_max
    p_max,mot=test_point(letters,p_max,dic,a,-1,-1,-1,-1,-1,-1)
    if p_max>p_anc: s=mot
    for b in range(7):
        if a!=b:
            p_anc=p_max
            p_max,mot=test_point(letters,p_max,dic,a,b,-1,-1,-1,-1,-1)
            if p_max>p_anc: s=mot
            elif p_max == p_anc and s!='' and mot !='':
                if list(dic).index(mot)<list(dic).index(s):
                    s=mot
        for c in range(7):
            if a!=b and a!=c and b!=c:
                p_anc=p_max
                p_max,mot=test_point(letters,p_max,dic,a,b,c,-1,-1,-1,-1)
                if p_max>p_anc: s=mot
                elif p_max == p_anc and s!='' and mot !='':
                    if list(dic).index(mot)<list(dic).index(s):
                        s=mot
            for d in range(7):
                if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
                    p_anc=p_max
                    p_max,mot=test_point(letters,p_max,dic,a,b,c,d,-1,-1,-1)
                    if p_max>p_anc: s=mot
                    elif p_max == p_anc and s!='' and mot !='':
                        if list(dic).index(mot)<list(dic).index(s):
                            s=mot
                for e in range(7):
                    if a!=b and a!=c and a!=d and a!=e and b!=c and b!=d and b!=e and c!=d and c!=e and d!=e:
                        p_anc=p_max
                        p_max,mot=test_point(letters,p_max,dic,a,b,c,d,e,-1,-1)
                        if p_max>p_anc: s=mot
                        elif p_max == p_anc and s!='' and mot !='':
                            if list(dic).index(mot)<list(dic).index(s):
                                s=mot
                    for f in range(7):
                        if a!=b and a!=c and a!=d and a!=e and a!=f and b!=c and b!=d and b!=e and b!=f and c!=d and c!=e and c!=f and d!=e and d!=f and e!=f:                            
                            p_anc=p_max
                            p_max,mot=test_point(letters,p_max,dic,a,b,c,d,e,f,-1)
                            if p_max>p_anc: s=mot
                            elif p_max == p_anc and s!='' and mot !='':
                                if list(dic).index(mot)<list(dic).index(s):
                                    s=mot
                        for g in range(7):
                            if a!=b and a!=c and a!=d and a!=e and a!=f and a!=g and b!=c and b!=d and b!=e and b!=f and b!=g and c!=d and c!=e and c!=f and c!=g and d!=e and d!=f and d!=g and e!=f and e!=g and f!=g:
                                p_anc=p_max
                                p_max,mot=test_point(letters,p_max,dic,a,b,c,d,e,f,g)
                                if p_max>p_anc: s=mot
                                elif p_max == p_anc and s!='' and mot !='':
                                    if list(dic).index(mot)<list(dic).index(s):
                                        s=mot
print(s)
