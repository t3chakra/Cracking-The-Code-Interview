def binarySearch(temp,searchValue,size):
    left=0
    right=size-1
    while(left<=right):
        mid=left+(right-left)/2
       # print left,right,mid
        if searchValue==temp[mid]:
            return mid-1
        elif searchValue<temp[mid]:
            right=mid-1
        elif searchValue>temp[mid]:
            left=mid+1
    return mid
        
                    
def flavourFinder(a,m,n):
    temp=sorted(a)
    result=[]
    index=binarySearch(temp,m,n)
    searchSpace=temp[0:index+1]
    for i in xrange(len(searchSpace)):
        x=searchSpace[i]
        if m-x in searchSpace[i+1:len(searchSpace)]:
            result.append(x)
            result.append(m-x)
            break
        
    if(result[0]!=result[1]):
        index1=a.index(result[0])+1
        index2=a.index(result[1])+1
        if index1<index2:
            print index1,index2
        else:
            print index2,index1
    else:
        indexList=[]
        for i in xrange(len(a)):
            if a[i]==result[0]:
                indexList.append(i+1)
            if len(indexList)==2:
                break
        if indexList[0]<indexList[1]:
            print indexList[0],indexList[1]
        else:
            print indexList[1],indexList[0]
            
t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    flavourFinder(a,m,n)
