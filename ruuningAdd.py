a,b=[int(x) for x in raw_input().strip().split()]
alist=list(bin(a))
blist=list(bin(b))
if len(blist) > len(alist):
    print 0
else:

    for i in range(len(blist)):
        if alist[i] != blist[i]:
            break
    r=alist[0:i]+['0' for j in range(i,len(blist))]
    l=r[2:len(r)]
    res=0
    power=len(l)-1
    for i in range(len(l)):
        res+=int(l[i])*2**power
        power-=1
    print res
