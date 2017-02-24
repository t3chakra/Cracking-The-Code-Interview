# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input().strip().split()[0])
arr=[int(x) for x in raw_input().split()]
arr=sorted(arr)
short=1000000000000
result=[]
for i in range(n-1):
    dif=abs(arr[i+1]-arr[i])
    if dif<short:
        result=[]
        short=abs(arr[i+1]-arr[i])
        result.append(arr[i])
        result.append(arr[i+1])
    elif dif==short:
        result.append(arr[i])
        result.append(arr[i+1])
for i in result:
    print i,
print
