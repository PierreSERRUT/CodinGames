#mime-type
#python

import sys
import math

ext={}
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # e: file extension
    # mt: MIME type.
    e,mt = input().split()
    ext.update({e.upper():mt})
    
for i in range(q):

    fname=[]
    tname = input()
    index=tname.rfind('.')
    if index==-1:
        fname.append(tname)
        fname.append('')
    else:
        fname.append(tname[:index])
        fname.append(tname[index+1:].upper())       
    if fname[1] in ext:
        print(ext[fname[1]])
    else:
        print("UNKNOWN")