#!/usr/bin/py
# Head ends here
def pairs(a,k):
    #a contains array of numbers and k is the value of difference
    count=0
    a1=set()
    for i in range(len(a)):
        if a[i]>k:
            a1.add(a[i]-k)
   # print a1,set(a)
    b=a1.intersection(set(a))
    count=len(b)
            
    return count    
        
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size=a[0]
    _k=a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b,_k)
