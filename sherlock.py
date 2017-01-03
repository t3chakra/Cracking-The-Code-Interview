def sum(array):
    s=0
    for i in array:
        s+=i
    return s
def sherlock(a,n):
    if n==1:
        print "YES"
        return
    elif n==2:
        print "NO"
        return
    else:
        sum1=sum(a[0:1])
        sum2=sum(a[2:n])
        for i in range(1,n-1):
            if sum1==sum2:
                print "YES"
                return
            sum1+=a[i]
            sum2-=a[i+1]
               
        print "NO"
        return
t=int(raw_input().strip())
for i in range(t):
    n=int(raw_input().strip())
    a=[int(x) for x in raw_input().strip().split()]
    sherlock(a,n)
