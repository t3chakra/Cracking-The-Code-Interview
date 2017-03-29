n=int(raw_input().strip())
arr=map(int,raw_input().strip().split())
arr=sorted(arr)
arr.reverse()
while len(arr)>0:
    print len(arr)
    for i in range(len(arr)):
        arr[i]=arr[i]-arr[-1]
        if arr[i]==0:
            break
    while i<len(arr):
        arr.pop()
    #print arr
    #print len(arr)
