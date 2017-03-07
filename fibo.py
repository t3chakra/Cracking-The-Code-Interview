
import math
t=int(raw_input().strip())
for i in range(t):
    fib=[1,1]
    x=int(raw_input().strip())
    if x==0 or x==1:
        print "IsFibo"
    elif x<0:
        print "IsNotFibo"
    else:
        while x>fib[1]:
            fib.append(fib[0]+fib[1])
            fib.remove(fib[0])
            
        if x==fib[1]:
            print "IsFibo"
        
        else:
            print "IsNotFibo"
