
def count_cut(rec):
    x=len(rec)
    c=0
    dif =rec[0]
    for i in range(x):
        if rec[i]>0:
            rec[i]=rec[i]-dif
        else:
            c+=1
    print x-c
    return c

n=int(raw_input().strip())
arr=map(int,raw_input().strip().split())
arr=sorted(arr)
arr.reverse()
print n
while len(arr)>1:
    for i in range(len(arr)):
        arr[i]=arr[i]-arr[-1]
        if arr[i]==0:
            break
    while i<len(arr):
        arr.pop()
    print arr
    print len(arr)

