#!/usr/bin/python3 
from operator import itemgetter 
import sys 
lastword = None 
lastcount = 0 
curword = None 
i=1
for line in sys.stdin: 
    line = line.strip() 
    curword, count = line.split('\t', 1) 
    count = int(count)
    #print("**",curword,str(count),"**")
    if lastword == curword: 
        lastcount += count 
    else: 
        if lastword: 
            print("{}\t{}".format(lastword, lastcount)) 
            lastcount = count 
        lastword = curword
if lastword == curword: 
    print("{}\t{}".format(lastword, lastcount))
