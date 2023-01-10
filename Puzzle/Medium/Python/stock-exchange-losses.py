#stock-exchange-losses
#python

import sys
import math
import bisect

market=[]

n = int(input())
for i in input().split():
    v = int(i)
    market.append(v)
print(market,file=sys.stderr, flush=True)

m_per_max=0
l_perte=[]
m_per=0
m_max=market[0]
for i in range(len(market)):
    if i!=0:
        if m_max<market[i]:
            m_max=market[i]
            bisect.insort(l_perte, -1*m_per)
            m_per=0
        else:
            m_per+=market[i-1]-market[i]
            if m_per_max<m_per:m_per_max=m_per
    print('m_perte:',m_per,file=sys.stderr, flush=True)

bisect.insort(l_perte, -1*m_per_max)
print(l_perte,file=sys.stderr, flush=True)



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(str(l_perte[0]))
