#!/bin/python
import sys
def count(S, m, n):
    for row in xrange(m):
        for col in xrange(1,n+1):
            if row>=1:
                x=table[row-1][col]
            else:
                x=0
            if col-S[row]>=0:
                y=table[row][col-S[row]]
            else:
                y=0
            table[row][col]=x+y
    
    return table[row][col]        
def make_change(coins, n):
    return count(coins,len(coins),n)    

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
coins = map(int,raw_input().strip().split(' '))
table=[[0 for col in xrange(n+1)]for row in xrange(m)]
for x in range(m):
    table[x][0]=1
print make_change(coins, n)
