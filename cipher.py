def decode(S,n,k):
    temp=[int(x) for x in S]
    r=[]
    xor=0
    for i in range(0,n):
        if i>=k:
            xor^=r[i-k]
        r.append(temp[i]^xor)
        xor^=r[-1]
    result=""
    for x in r:
        result+=str(x)
    print result
N,K=raw_input().strip().split()
N=int(N)
K=int(K)
S=raw_input().strip()
decode(S,N,K)
