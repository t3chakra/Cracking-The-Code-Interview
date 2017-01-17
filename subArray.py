def sumArray(asum):
    sum=0
    for i in range(len(asum)):
        sum+=asum[i]
    return sum
def subArray(a,m,n):

    temp2=set()
    power_set_size=2**n
    for i in range(1,power_set_size):
        temp1 = []
        for j in range(n):
                if i &(1<<j):
                    temp1.append(a[j])
        temp2.add(sumArray(temp1)%m)
    #     print temp1,temp2
    # print temp2
    print max(temp2)



n,m=[int(x)for x in raw_input().strip().split()]
a=[int(x) for x in raw_input().split()]
a=sorted(a)
subArray(a,m,n)