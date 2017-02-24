import time
a,b=[int(x) for x in raw_input().strip().split()]
start=time.time()
# c=a
# for i in range(a,b+1):
#     print c,i
#     c=c&i;
# print c
# alist=list(bin(a))
# blist=list(bin(b))
# if len(blist) > len(alist):
#     print 0
# else:
#
#     for i in range(len(blist)):
#         if alist[i] != blist[i]:
#             break
#     r=alist[0:i]+['0' for j in range(i,len(blist))]
#     l=r[2:len(r)]
#     res=0
#     power=len(l)-1
#     for i in range(len(l)):
#         res+=int(l[i])*2**power
#         power-=1
#     print res
shift=0
while a!=b:
    a=a>>1
    b=b>>1
    shift+=1;
print a<<shift
end=time.time()
print end-start