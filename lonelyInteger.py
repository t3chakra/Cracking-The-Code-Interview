#!/bin/python

import sys

def lonely_integer(a):
    value=0
    for i in a:
        value=value^i
    return value
      

n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
print lonely_integer(a)
