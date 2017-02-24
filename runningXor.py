#finding xor numbers in a range from 1 to b
def f(n):
    res=[n,1,n+1,0]
    return res[n%4]
a,b=[int(x) for x in raw_input().strip().split()]

print f(a-1)^f(b)
