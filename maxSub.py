n,k=map(int,raw_input().strip().split())
a=map(int,raw_input().strip().split())
max=n
equal=0
count={}
for i in a:
    if i%k in count:
        count[i%k]+=1
    else:
        count[i%k]=1
print count
for key in count:
    if key==0 or key==k-key:
        max=max-count[key]+1
    elif k-key in count and count[k-key]>count[key]:
        max=max-count[key]
    elif k-key in count and count[k-key]==count[key]:
        equal+=count[k-key]
print max-equal//2