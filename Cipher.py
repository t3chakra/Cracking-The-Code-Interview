def decode(S,n,k):
    temp=[int(x) for x in S]
    r=[]
    r.append(temp[0])
    for i in range(1,n-1):
        xor=0
        if i>=k-1:
            for j in range(i-k+1,i):
                xor=xor^r[j]
            r.append(xor^temp[i])
        else:         
            for j in range(0,i):
                xor=xor^r[j]               
            r.append(xor^temp[i])
    r.append(temp[-1])
    result=""
    for x in r:
        result+=str(x)
    print result
N,K=raw_input().strip().split()
N=int(N)
K=int(K)
S=raw_input().strip()
decode(S,N,K)
