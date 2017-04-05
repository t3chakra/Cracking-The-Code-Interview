#!/bin/python
import sys
def findA(s):
    sList=list(s)
    frq=0
    for c in sList:
        if c=='a':
            frq+=1
    return frq
s = raw_input().strip()
n = long(raw_input().strip())
fulStr=n//len(s)
left=n%len(s)
newStr=s[:left]

print findA(s)*fulStr+findA(newStr)