def number_needed(a, b):
    freq={}
    for i in range(97,97+26):
        freq[chr(i)]=0
    #print freq   
    for i in xrange(len(a)):
        freq[a[i]]+=1
    for j in xrange(len(b)):
        freq[b[j]]-=1
    count=0    
    for i in freq:
        if freq[i]!=0:
            count+=abs(freq[i])
      
    return count
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
