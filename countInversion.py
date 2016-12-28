def msort(a,n):
    if n==1:
        return a,0
    else:
        mid=n/2
        L=a[:mid]
        R=a[mid:]
        L,x=msort(L,mid)
        R,y=msort(R,n-mid)
        D,z=merge(L,R,n,mid)
        return D,x+y+z
def merge(L,R,n,mid):
    D=[None]*n
    i=j=0
    countInv=0
    for k in range(n):
        if i<mid and j<n-mid:
            if L[i]>R[j]:
                D[k]=R[j]
                j+=1
                countInv+=mid-i
            else:
                D[k]=L[i]
                i+=1
        elif i>=mid:
            D[k]=R[j]
            j+=1
        else:
            D[k]=L[i]
            i+=1
    return D,countInv
def count_inversions(a):
    return msort(a,len(a))

    
      

t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    print count_inversions(arr)[1]
    
